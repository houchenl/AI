#-*- coding:utf-8 -*-

import re

#处理页面标签类
class Tool(object):
    #img标签或者长空格
    ImgPattern=re.compile('<img.*?>|\s{7}')
    #超链接(a标签)
    APattern=re.compile('<a.*?>|</a>')
    #div,tr或者p
    LinePattern=re.compile('<tr>|<div>|</div>|</p>')
    #<td>标签
    TdPattern=re.compile('<td>')
    #p标签
    ParaPattern=re.compile('<p.*?>')
    #多个br标签
    BrPattern=re.compile('<br><br>|<br>')
    #其余标签
    ExtraPattern=re.compile('<.*?>')

    def replace(self,x):
        #去除img标签及7位空格
        x=self.ImgPattern.sub("",x)
        #去除a标签
        x=self.APattern.sub("",x)
        #将换行的标签换成\n
        x=self.LinePattern.sub("\n",x)
        #将td换成\t
        x=self.TdPattern.sub("\t",x)
        #段落开头换位\n加两空格
        x=self.ParaPattern.sub("\n  ",x)
        #将换行符或双换行符换成\n
        x=self.BrPattern.sub("\n",x)
        #将其余标签剔除
        x=self.ExtraPattern.sub("",x)
        return x.strip()



#-------新改版的淘女郎页面抓取原理及攻略-------

craw_principle="""
新改版的淘女郎页面，不是通过url上传递页面参数，如?page=2,来跳到下一页的。
而是通过ajax提交form数据，如currentPage:2来获取指定页面的淘女郎信息
通过ajax请求，返回的是包含请求页面的所有淘女郎的个人信息，数据类型为json
处理ajax的url为：https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8，不传数据，默认第一页淘女郎

现在分析下返回的json数据：
淘女郎数据在一个searchDOList列表内，列表内为多个字典，每个字典为一个淘女郎个人信息，包含头像，
"userId":129361161（这个很重要），因为前面加上BaseURL:'https://mm.taobao.com/self/aiShow.htm?spm=0.0.0.0.c86RlF'就成为
淘女郎个人详情页面，如BaseURL+'&'+'userId',得到'https://mm.taobao.com/self/aiShow.htm?spm=0.0.0.0.c86RlF&userId=129361161'
此为淘女郎详情页面url

现在分析下需要提交给ajax的数据:
一共如下
q:
viewFlag:A
sortType:default
searchStyle:
searchRegion:city:
searchFansNum:
currentPage:1
pageSize:100

python解析json数据
import json
postData={'q':'','viewFlag':'A','sortType':'defaul't,'searchStyle':'','searchRegion':'city:','searchFansNum':'',
'currentPage':1,'pageSize':100}
postData=urllib.urlencode(postData)
ajaxURL='https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
request=urllib2.Request(url=ajaxURL,data=postData)
response=urllib2.urlopen(request).read().decode('utf-8')
data=json.loads(response)
从data中提取想要的数据即可
"""

# import json
# data={"data":{
#     "currentPage":1,
#     "searchContents":"{viewFlag:A,searchStyle:null,searchRegion:null,searchFansNum:null}",
#     "searchDOList":[{"avatarUrl":"//gtd.alicdn.com/sns_logo/i8/TB1fAoAIFXXXXaPXXXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i3/TB15bUwIFXXXXagXpXXSutbFXXX.jpg","city":"杭州市","height":"165.0","identityUrl":"1,2,4,5,","modelUrl":"","realName":"凌智贤","totalFanNum":808,"totalFavorNum":18542,"userId":129361161,"viewFlag":"W M D S F ","weight":"43"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i5/TB1im4EIpXXXXaaXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i1/TB16bDJHFXXXXX2XFXXSutbFXXX.jpg","city":"杭州市","height":"165","identityUrl":"","modelUrl":"","realName":"张恋恋","totalFanNum":461,"totalFavorNum":2946,"userId":251515131,"viewFlag":"N","weight":"45"},{"avatarUrl":"//img.alicdn.com/sns_logo/i4/TB1Te6.GFXXXXbXaXXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i7/T1S7aOXCdaXXb1upjX.jpg","city":"杭州市","height":"165.0","identityUrl":"1,2,3,4,","modelUrl":"","realName":"杨杨","totalFanNum":172159,"totalFavorNum":17008,"userId":508201028,"viewFlag":"W M D Z S ","weight":"44"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i1/TB1uJHyIXXXXXXmXVXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i7/TB1EAstFVXXXXaDXVXXSutbFXXX.jpg","city":"杭州市","height":"170","identityUrl":"","modelUrl":"","realName":"秦小顺","totalFanNum":53,"totalFavorNum":10261,"userId":166735626,"viewFlag":"N","weight":"50"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i5/TB12GWYIFXXXXarapXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i6/TB1N2YiIFXXXXaeXpXXSutbFXXX.jpg","city":"广州市","height":"172","identityUrl":"1,2,5,","modelUrl":"","realName":"E列娜","totalFanNum":186,"totalFavorNum":17339,"userId":669539593,"viewFlag":"W M D F ","weight":"49"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i5/TB1vrZbIFXXXXcpXVXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i2/TB1KIglIpXXXXaxXFXXSutbFXXX.jpg","city":"广州市","height":"168","identityUrl":"1,","modelUrl":"","realName":"Alona-","totalFanNum":53,"totalFavorNum":2932,"userId":1798453353,"viewFlag":"W M ","weight":"46"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i4/TB1g8pEIFXXXXXRXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i7/TB1bXEMGXXXXXczXXXXSutbFXXX.jpg","city":"杭州市","height":"167","identityUrl":"1,","modelUrl":"","realName":"董俐DONG","totalFanNum":105,"totalFavorNum":6171,"userId":1673648976,"viewFlag":"W M ","weight":"47"},{"avatarUrl":"//img.alicdn.com/sns_logo/i1/T1K9T7FfVeXXb1upjX.jpg","cardUrl":"//img.alicdn.com/imgextra/i2/12995063006845876/TB1pvkdGVXXXXbYXFXXXXXXXXXX_!!504722995-0-tstar.jpg","city":"成都市","height":"165.0","identityUrl":"1,2,3,","modelUrl":"","realName":"莎莎","totalFanNum":2024230,"totalFavorNum":5410,"userId":504722995,"viewFlag":"W M D Z ","weight":"45.0"},{"avatarUrl":"//img.alicdn.com/sns_logo/i8/TB1jfg4GVXXXXXYXFXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i4/T16BHcFAVaXXb1upjX.jpg","city":"杭州市","height":"168","identityUrl":"2,5,","modelUrl":"","realName":"陈洁kiki","totalFanNum":716,"totalFavorNum":15482,"userId":2014901629,"viewFlag":"W D F ","weight":"48.0"},{"avatarUrl":"//img.alicdn.com/sns_logo/i3/TB1ej4BHpXXXXXwXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i3/11947031865468803/T1TM0fFxhbXXXXXXXX_!!290551947-0-tstar.jpg","city":"广州市","height":"166.0","identityUrl":"1,2,3,","modelUrl":"","realName":"rikki","totalFanNum":141387,"totalFavorNum":29300,"userId":290551947,"viewFlag":"W M D Z ","weight":"42.0"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i6/TB1yEczIpXXXXXKXVXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i1/TB1XQLoHVXXXXaAXFXXwu0bFXXX.png","city":"广州市","height":"171","identityUrl":"","modelUrl":"","realName":"模特萱萱","totalFanNum":27,"totalFavorNum":1534,"userId":2520033966,"viewFlag":"N","weight":"47"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i7/TB15kRrIpXXXXalXVXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i8/T1v.OMXEFbXXb1upjX.jpg","city":"杭州市","height":"166.0","identityUrl":"1,2,3,","modelUrl":"","realName":"玥儿","totalFanNum":126807,"totalFavorNum":13325,"userId":125808639,"viewFlag":"W M D Z ","weight":"46.0"},{"avatarUrl":"//img.alicdn.com/sns_logo/i2/T1Hxa4FN4bXXb1upjX.jpg","cardUrl":"//img.alicdn.com/imgextra/i7/T1sKVlFEBcXXb1upjX.jpg","city":"厦门市","height":"162.0","identityUrl":"2,4,","modelUrl":"","realName":"厦门柒柒","totalFanNum":5856,"totalFavorNum":4846,"userId":240575018,"viewFlag":"W D S ","weight":"41.0"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i6/TB1JskEIpXXXXb_XFXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i7/TB1DDAKIpXXXXbOXpXXSutbFXXX.jpg","city":"杭州市","height":"170","identityUrl":"4,","modelUrl":"","realName":"隋潇漪","totalFanNum":28,"totalFavorNum":2712,"userId":482498316,"viewFlag":"W S ","weight":"44"},{"avatarUrl":"//img.alicdn.com/sns_logo/i3/T1VfxPFnJgXXaCwpjX.png","cardUrl":"//img.alicdn.com/imgextra/i4/T18iROFn8eXXb1upjX.jpg","city":"杭州市","height":"165.0","identityUrl":"1,2,4,5,","modelUrl":"","realName":"余潇潇","totalFanNum":2946,"totalFavorNum":4349,"userId":355499374,"viewFlag":"W M D S F ","weight":"45.0"},{"avatarUrl":"//img.alicdn.com/sns_logo/i1/TB1vxvxGVXXXXbGXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i2/TB1Yg9RGVXXXXaBXXXXSutbFXXX.jpg","city":"西安市","height":"168","identityUrl":"","modelUrl":"","realName":"桃子kia","totalFanNum":356,"totalFavorNum":2705,"userId":400959368,"viewFlag":"N","weight":"42"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i4/TB1ka7vHVXXXXX8XpXXSutbFXXX.jpg","cardUrl":"","city":"温州市","height":"","identityUrl":"","modelUrl":"","realName":"VERA薇薇","totalFanNum":4,"totalFavorNum":4917,"userId":480115274,"viewFlag":"N","weight":""},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i5/TB1QtnQHFXXXXccXpXXwu0bFXXX.png","cardUrl":"//img.alicdn.com/imgextra/i6/TB17EHeHXXXXXa4aXXXwu0bFXXX.png","city":"杭州市","height":"160","identityUrl":"","modelUrl":"","realName":"mini宛妮","totalFanNum":380,"totalFavorNum":3415,"userId":382249885,"viewFlag":"N","weight":"40"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i4/TB1rZT7HFXXXXcOXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i3/TB1i7c9HpXXXXb4XpXXSutbFXXX.jpg","city":"杭州市","height":"172","identityUrl":"","modelUrl":"","realName":"张馨元M","totalFanNum":79,"totalFavorNum":9837,"userId":152149350,"viewFlag":"N","weight":"54.0"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i6/TB1lXQDIpXXXXbRaXXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i7/TB1e1L2IFXXXXcLXFXXSutbFXXX.jpg","city":"杭州市","height":"165","identityUrl":"","modelUrl":"","realName":"何紫晴","totalFanNum":39,"totalFavorNum":1170,"userId":927115494,"viewFlag":"N","weight":"40"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i7/TB1WK.VIXXXXXaHXXXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i8/TB1t40XGpXXXXagXpXXSutbFXXX.jpg","city":"广州市","height":"163","identityUrl":"1,","modelUrl":"","realName":"小熊JJ","totalFanNum":83,"totalFavorNum":169,"userId":1030013886,"viewFlag":"W M ","weight":"42"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i5/TB1tRb5IFXXXXaYXVXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i3/TB1qcgZGVXXXXbvXFXXSutbFXXX.jpg","city":"杭州市","height":"164","identityUrl":"2,4,","modelUrl":"","realName":"程柳青","totalFanNum":1260,"totalFavorNum":5063,"userId":132298952,"viewFlag":"W D S ","weight":"48"},{"avatarUrl":"//img.alicdn.com/sns_logo/i6/T1cCR5Xr0fXXb1upjX.jpg","cardUrl":"","city":"北京市","height":"164.0","identityUrl":"2,4,","modelUrl":"","realName":"伊伊","totalFanNum":11131,"totalFavorNum":2841,"userId":575078231,"viewFlag":"W D S ","weight":"44.0"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i3/TB1KBoLIpXXXXaXXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i8/TB1Db3mGVXXXXXcapXXwu0bFXXX.png","city":"广州市","height":"172","identityUrl":"","modelUrl":"","realName":"模特韩雪","totalFanNum":18,"totalFavorNum":5523,"userId":2461335164,"viewFlag":"N","weight":"46"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i2/TB1Pd3zIpXXXXa2XFXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i1/T1HvsiXg0eXXb1upjX.jpg","city":"广州市","height":"170.0","identityUrl":"1,2,","modelUrl":"","realName":"程茜如","totalFanNum":1012,"totalFavorNum":29741,"userId":1056775387,"viewFlag":"W M D ","weight":"47"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i7/TB1ZmCJIFXXXXalXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i7/T1e8aUXvXeXXb1upjX.jpg","city":"杭州市","height":"168","identityUrl":"1,2,3,","modelUrl":"","realName":"一柳hz","totalFanNum":1509,"totalFavorNum":15741,"userId":196332289,"viewFlag":"W M D Z ","weight":"47"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i3/TB1HSdbIpXXXXciXpXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i1/TB1WNFNGVXXXXXDXFXXSutbFXXX.jpg","city":"杭州市","height":"160","identityUrl":"","modelUrl":"","realName":"青橙0921","totalFanNum":63,"totalFavorNum":1138,"userId":1627864142,"viewFlag":"N","weight":"45"},{"avatarUrl":"//img.alicdn.com/sns_logo/i3/TB1fq__GVXXXXaSXFXXSutbFXXX.jpg","cardUrl":"//img.alicdn.com/imgextra/i2/TB1BJ62GFXXXXXvXpXXSutbFXXX.jpg","city":"杭州市","height":"165.0","identityUrl":"1,4,","modelUrl":"","realName":"Z珍珍","totalFanNum":978,"totalFavorNum":1875,"userId":203036173,"viewFlag":"W M S ","weight":"46.0"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i4/TB1CS9lIFXXXXb_XFXXwu0bFXXX.png","cardUrl":"//img.alicdn.com/imgextra/i1/TB1l79DIFXXXXXMXXXXSutbFXXX.jpg","city":"杭州市","height":"167","identityUrl":"","modelUrl":"","realName":"林静敏KR","totalFanNum":1,"totalFavorNum":8465,"userId":479100570,"viewFlag":"N","weight":"44"},{"avatarUrl":"//gtd.alicdn.com/sns_logo/i1/TB1dYTVIpXXXXbLXpXXwu0bFXXX.png","cardUrl":"","city":"杭州市","height":"164","identityUrl":"","modelUrl":"","realName":"高娜丽","totalFanNum":83,"totalFavorNum":31528,"userId":391504976,"viewFlag":"N","weight":"46"}],
#     "searchText":"",
#     "totalCount":40331,
#     "totalPage":1345
#     },
# "message":"search success!",
# "status":1
# }
# data2=json.loads(data)
# print data2































