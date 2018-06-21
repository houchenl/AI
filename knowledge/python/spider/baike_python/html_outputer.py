# -*- coding:utf-8 -*-

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write('<html>')

        # 需要指定网页编码，否则打开网页看到的中文是乱码
        fout.write('<head>')
        fout.write('<meta charset="UTF-8">')
        fout.write('</head>')

        fout.write('<body>')
        fout.write('<table>')

        # python default encoding is ascii
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('UTF-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('UTF-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
