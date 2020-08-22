from django.shortcuts import render
from apps.message_form.models import Message


def message_form(request):
    # # 1. 用all，返回的是queryset，可以用for循环遍历，也可以做切片
    # all_messages = Message.objects.all()
    #
    # # 2. 用filter，相当于where语句，会找出所有符合条件的，如果没有的话，返回空queryset
    # all_messages = Message.objects.filter(name='wangi')
    # # 删除得到的数据
    # # all_messages.delete()
    #
    # for message in all_messages:
    #     # 逐条删除数据
    #     # message.delete()
    #     print(message.name)
    #
    # # 3. 用get，返回的是一个对象，不能用for循环遍遍历，如果找不到对象，会抛出异常
    # message = Message.objects.get(name = 'wangi')
    # print(message.address)
    #
    # # 进行数据插入操作
    # message = Message()
    # message.name = 'zicheng'
    # message.email = 'zicheng@gmail.com'
    # message.address = 'zicheng street zicheng room'
    # message.message = 'wangi is beautiful'
    # # 如果存在则更新，如果不存在则插入
    # message.save()
    if request.method == 'POST':
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        content = request.POST.get("message", "")

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = content
        message.save()

        var_dict = {
            "message": message
        }

        return render(request, "message_form.html", var_dict)

    if request.method == "GET":
        var_dict = {}
        all_messages = Message.objects.all()
        if all_messages:
            message = all_messages[0]
            var_dict = {
                "message": message
            }
        return render(request, "message_form.html", var_dict)