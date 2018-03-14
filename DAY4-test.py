import orm
from models import User
import asyncio
"""
DAY4 数据测试代码
"""
async def test(loop):
    # 创建连接池
    db_dict = {'user': 'root', 'password': 'hkj19651216', 'db': 'awesome'} # user
    await orm.create_pool(loop=loop, **db_dict)
    u = User(name='Test', email='test14@example.com', passwd='12345', image='about:blank', id='14')
    await u.save()
    await orm.close_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()