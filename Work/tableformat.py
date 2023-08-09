# tableformat.py

class TableFormatter:
    def headings(self, headers):
        """
        테이블 헤딩을 반환
        """
        raise NotImplementedError()
    def row(self, rowdata):
        """
        테이블 데이터의 단일 행을 반환.
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Output data in plain-text format.
    테이블을 일반 텍스트 포맷으로 출력
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ' * len(headers)))
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    포트폴리오 데이터를 CSV 포맷으로 출력.
    '''
    def headings(self, headers):
        print(','.join(headers))
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)

















