class FromDataAdapter:
    def __init__(self, filepath):
        self.filepath = filepath

    def convert_from_txt_to_html(self):
        with open(self.filepath) as file:
            lines = file.readlines()
        tags_txt = lines[0].replace('\n', '')
        user_data_txt = lines[1:]
        data_txt = [item.replace('\n', '').split(',') for item in user_data_txt]
        header = tags_txt.split(',')
        result = []
        for row in data_txt:
            for i in range(len(header)):
                result.append(f'<{header[i]}>{row[i]}</{header[i]}>')
        for row in result:
            print(row)


if __name__ == '__main__':
    data = FromDataAdapter('data.txt').convert_from_txt_to_html()
