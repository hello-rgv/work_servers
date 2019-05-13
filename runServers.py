'''
@Author: Mr Bean
@Date: 2019-05-12 00:37:23
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 15:13:58
@Description: file content
'''

import sys
from App import create_app
from App.api.baseInfo.goods import Goods as goodsBluePrint
from App.api.baseInfo.unit import Unit as unitBluePrint

app = create_app()
app.register_blueprint(goodsBluePrint, url_prefix='/api/baseInfo/goods')
app.register_blueprint(unitBluePrint, url_prefix='/api/baseInfo/unit')

if __name__ == '__main__':
    # 为项目添加临时路径, 如果不添加会出现子目录(包)找不到父级包的情况
    sys.path.append(app.config['BASE_DIR'])
    app.run()
