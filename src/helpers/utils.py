class Utils:
    @staticmethod
    def month_converter(month):
        months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        if month in months:
            return months.index(month) + 1
        else:
            return 0