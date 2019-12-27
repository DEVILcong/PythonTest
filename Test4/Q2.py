class handleDate:
    def __init__(self, date):
        print(date)
        if((date[0])%4 == 0 and (date[0])%100 != 0) or (date[0])%400 == 0:
            self.isLeap = 1
        else:
            self.isLeap = 0
        
        if date[1] > 12:
            print('ERROR')
            return

        if self.isLeap == 1:
            if date[2] > self._leapMonth[date[1] - 1]:
                print('ERROR')
                return
        else:
            if date[2] > self._month[date[1] - 1]:
                print('ERROR')
                return
        
        self._date[0] = date[0]
        self._date[1] = date[1]
        self._date[2] = date[2]

    def chooseMonth(self):
        '''
        选择要使用哪一个月份天数列表
        '''
        if self._isLeap == 1:
            return self._leapMonth
        else:
            return self._month
    def plusDay(self, M, D, days):
        month = self.chooseMonth()
        if D + days < month[M-1]:
            return M, D + days
        else:
            days = days - (month[M-1] - D)
            M = M + 1
            D = 0
            while days - month[M-1] >= 0:
                days = days - month[M-1]
                M = M + 1
            if days == 0:
                M = M - 1
                D = month[M-1]
            else:
                D = D + days

            return M, D
    _date = [0, 0, 0]
    _isLeap = 0
    _month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _leapMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
