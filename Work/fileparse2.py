# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    CSV 파일을 파싱 및 형변환하여 레코드의 리스트를 생성.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    # 파일 헤더가 있으면 읽음
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    # 특정 컬럼을 선택한 경우, 필터링을 위한 인덱스를 만들고 출력 컬럼을 설정
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data  데이터가 없는 행을 건너뜀
            continue

        # If specific column indices are selected, pick them out
        # 특정 컬럼 인덱스가 선택되었으면 그것을 고름
        if select:
            row = [row[index] for index in indices]

        # Apply type conversion to the row
        # 행에 형변환을 적용
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple
        # 튜플의 딕셔너리를 만듦
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records

