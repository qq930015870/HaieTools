
class Base:
    @staticmethod
    def is_number(s):
        """
        判断是否为数字
        :return:是数字返回True,不是数字返回False
        """
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

