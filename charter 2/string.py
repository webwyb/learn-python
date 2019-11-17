# /*
#  * @Author: wuyanbin beijingwyb@163.com 
#  * @Date: 2019-11-16 22:30:07 
#  * @Last Modified by:   wuyanbin beijingwyb@163.com 
#  * @Last Modified time: 2019-11-16 22:30:07 
#  */
# 变量类型1 字符串
str = 'this is string'
print(str)
print('===')

# 一.字符串方法 - 1.修改字符串大小写

varible = 'hello wuyanbin'
# 将字符串首字母大写  Hello Wuyanbin
print(varible.title());
# 将字符串全部大写  HELLO WORLD
print(varible.upper());
# 将字符串全部小写  hello world
print(varible.lower());

print('===')
# 一.字符串方法 - 2.合并（拼接）字符串

first_name = 'wu'
last_name = 'yanbin'
full_name = first_name + last_name + '!'
print(full_name)

print('===')
# 一.字符串方法 - 3.特殊符号 \t: 制表符 \n:换行符
print('\twu')
print('\nwu\t\twu')

print('===')
# 一.字符串方法 - 4.去除字符串空白

lang_with_space = ' python '
# 去除字符串末尾空白 rstrip() ==> right strip(右侧：末尾)
print(lang_with_space.rstrip())
# 去除字符串开头空白 lstrip() ==> left strip(左侧：开头)
print(lang_with_space.lstrip())
# 去除字符串两端空白 strip()
print(lang_with_space.strip())