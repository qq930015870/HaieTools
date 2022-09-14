import sys
import os
import json

import pandas as pd
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout,QFileDialog,QTableWidgetItem
from ToLinksTools import Ui_Form

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.resultShowView.hide()
        self.form.result_lable.hide()
        self.show()

    def addItemForTable(self):
        pass

    # 判断是否是中文
    def isChinesse(self,str):

        for ch in str:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False

    # 清洗字符串中的中文及符号
    def cleanSku(self,str):
        content = str
        for i in range(len(content)):
            if self.isChinesse(content[i]):
                content.re
            elif content[i] == "（":
                content[i] = ""
            elif content[i] == "）":
                content[i] = ""
            elif content[i] == "(":
                content[i] = ""
            elif content[i] == ")":
                content[i] = ""
        return content

    # 获取型号零售价
    def getSalesPrice(self,sku_id):
        with open("price.json","r",encoding="utf-8") as f:
            content = f.read()
        price_dict = json.dumps(content)
        print(price_dict)
        print(type(price_dict))
        # print(price_dict)
        # sale_price = price_dict[str(sku_id)]
        # return sale_price

    # 获取文件地址文本框的内容
    def getTextFromEdit(self):
        return self.form.promotionFilePath.text()

    # 按钮点击事件-打开文件函数
    def showChoosePromotionFile(self):
        fname,_ = QFileDialog.getOpenFileName(self,"打开文件",".","*.xls *.xlsx")
        self.form.promotionFilePath.setText(fname)

    # 读取活动文件
    def readPromotionFile(self):
        # self.form.resultShowView.hide()
        self.form.result_lable.hide()
        # self.form.result_lable.show()
        self.form.resultTable.show()
        filepath = self.form.promotionFilePath.text()
        data = pd.read_excel(filepath)
        self.form.resultTable.setRowCount(data.shape[0])
        for index,value in data.iterrows():
            col = 0
            for v in value:
                item = QTableWidgetItem(str(v))
                self.form.resultTable.setItem(index,col,item)
                col+=1

    # 生成链接
    def toLinksAction(self):
        row_count = self.form.resultTable.rowCount()
        result = []
        for i in range(row_count):
            brand = self.form.resultTable.item(i,0).text()
            catelog = self.form.resultTable.item(i,1).text()
            # sku_id 京东编码
            sku_id = self.form.resultTable.item(i,2).text()
            sku_id = self.cleanSku(sku_id)
            model_name = self.form.resultTable.item(i,3).text()
            sale_price = str(self.getSalesPrice(sku_id))
            price = self.form.resultTable.item(i,4).text()
            if self.form.resultTable.item(i,5).text() != "nan":
                promotion = self.form.resultTable.item(i,5).text()
            else:
                promotion = "令牌价"
            date_range = self.form.resultTable.item(i,6).text()

            res = """
%s%s%s
前台：%s 
令牌：%s（%s）
链接：https://item.jd.com/%s.html
-----------------------------------"""%(brand,catelog,model_name,sale_price,price,promotion,sku_id)

            result.append(res)

        # with open("temp.txt","a+",encoding="utf-8") as f:
        #     for item in result:
        #         f.write(item)
        content = ""
        for item in result:
            content = content + item
        self.form.resultShowView.setPlainText(content)
        self.form.result_lable.show()
        self.form.resultTable.hide()
        self.form.label_3.hide()
        self.form.resultShowView.show()

        print("程序执行成功！")

    # 全选
    def selectAll(self):
        self.form.resultShowView.selectAll()

    # 全部复制
    def copyAll(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.form.resultShowView.toPlainText())

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
