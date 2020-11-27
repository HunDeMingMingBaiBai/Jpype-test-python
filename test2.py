import jpype
import time

def buildComplexObject():
    complexObject = ComplexObject()
    complexObject.setIntValue(Integer(1))
    complexObject.setLongValue(1)
    complexObject.setDoubleValue(1.0)
    complexObject.setStr("hello 1")
    listInParam = ArrayList()
    listInParam.add(1)
    listInParam.add(3)
    listInParam.add(5)
    complexObject.setList(listInParam)
    map = HashMap()
    map.put("int", Integer(1))
    map.put("double", 1)
    map.put("str", "hello 1")
    complexObject.setMap(map)
    data = Data()
    data.setData("hello data 1")
    complexObject.setData(data)
    return complexObject


if __name__ == '__main__':
    jvmArg = '-Djava.class.path=/Users/4paradigm/IdeaProjects/Jpype-test/out/artifacts/Jpype_test_jar/Jpype-test.jar'
    print(jpype.getDefaultJVMPath())
    if not jpype.isJVMStarted():
        jpype.startJVM(jpype.getDefaultJVMPath(), jvmArg)
    Test1 = jpype.JClass('com.paradigm.jpype.Test1')
    test = Test1()
    for i in range(10):
        start = time.time()
        result = test.run1(100000)
        end = time.time()
        print('--- --- ---')
        print(result)
        print(end - start)
        print((end - start) * 1000)
        print('--- --- ---')

    '''数据结构测试 map'''
    Test2 = jpype.JClass('com.paradigm.jpype.Test2')
    Data = jpype.JClass('com.paradigm.jpype.Data')
    HashMap = jpype.JClass("java.util.HashMap")
    ArrayList = jpype.JClass("java.util.ArrayList")
    Integer = jpype.JClass("java.lang.Integer")
    param = HashMap()
    list = ArrayList()
    list.add(1)
    list.add(3)
    list.add(5)
    data = Data()
    data.setData("hello data 1")
    test2 = Test2()
    param.put("int", Integer(1))
    param.put("double", 1.0)
    param.put("list", list)
    param.put("str", "hello1")
    param.put("data", data)
    result = test2.testMap(param)
    print(result)
    print(result.get("int"))
    print(result.get("double"))
    resultList = result.get("list")
    print("list start")
    for i in resultList:
        print(i)
    print("list end")
    resultData = result.get("data")
    print(resultData.getData())
    print('--- --- ---')

    '''数据结构测试 list'''
    list = ArrayList()
    list.add(Integer(1))
    list.add(1.0)
    list.add("hello 1")
    listInParam = ArrayList()
    listInParam.add(1)
    listInParam.add(3)
    listInParam.add(5)
    list.add(listInParam)
    map = HashMap()
    map.put("int", Integer(1))
    map.put("double", 1)
    map.put("str", "hello 1")
    list.add(map)
    data = Data()
    data.setData("hello data 1")
    list.add(data)
    resultList = test2.testList(list)
    print(resultList)
    print(resultList[0])
    print(resultList[1])
    print(resultList[2])
    print("list start")
    for i in resultList[3]:
        print(i)
    print("list end")
    print("map start")
    for entry in resultList[4].entrySet():
        print(entry.getKey() + " : " + str(entry.getValue()))
    print("map end")
    resultData = resultList[5]
    print(resultData.getData())
    print('--- --- ---')

    '''数据结构测试 ComplexObject'''
    ComplexObject = jpype.JClass("com.paradigm.jpype.ComplexObject")
    complexObject = ComplexObject()
    complexObject.setIntValue(Integer(1))
    complexObject.setLongValue(1)
    complexObject.setDoubleValue(1.0)
    complexObject.setStr("hello 1")
    listInParam = ArrayList()
    listInParam.add(1)
    listInParam.add(3)
    listInParam.add(5)
    complexObject.setList(listInParam)
    map = HashMap()
    map.put("int", Integer(1))
    map.put("double", 1)
    map.put("str", "hello 1")
    complexObject.setMap(map)
    data = Data()
    data.setData("hello data 1")
    complexObject.setData(data)
    resultObject = test2.testComplexObject(complexObject)
    print(resultObject)
    print(resultObject.getIntValue())
    print(resultObject.getLongValue())
    print(resultObject.getDoubleValue())
    print(resultObject.getStr())
    print("list start")
    for i in resultObject.getList():
        print(i)
    print("list end")
    print("map start")
    for entry in resultObject.getMap().entrySet():
        print(entry.getKey() + " : " + str(entry.getValue()))
    print("map end")
    resultData = resultObject.getData()
    print(resultData.getData())
    print('--- --- ---')

    '''数据结构测试 map2'''
    param = HashMap()
    list = ArrayList()
    list.add(1)
    list.add(3)
    list.add(5)
    map = HashMap()
    map.put("int", Integer(1))
    map.put("double", 1)
    map.put("str", "hello 1")
    object = buildComplexObject()
    param.put("map", map)
    param.put("list", list)
    param.put("object", complexObject)
    result = test2.testMap2(param)
    print(result)
    print("list start")
    for i in result.get("list"):
        print(i)
    print("list end")
    print("map start")
    for entry in result.get("map").entrySet():
        print(entry.getKey() + " : " + str(entry.getValue()))
    print("map end")
    print(result.get("object"))
    print('--- --- ---')

    '''数据结构测试 list2'''
    param = ArrayList()
    list = ArrayList()
    list.add(1)
    list.add(3)
    list.add(5)
    map = HashMap()
    map.put("int", Integer(1))
    map.put("double", 1)
    map.put("str", "hello 1")
    object = buildComplexObject()
    param.add(map)
    param.add(list)
    param.add(object)
    result = test2.testList2(param)
    print(result)
    print("map start")
    for entry in result.get(0).entrySet():
        print(entry.getKey() + " : " + str(entry.getValue()))
    print("map end")
    print("list start")
    for i in result.get(1):
        print(i)
    print("list end")
    print(result.get(2))
    print('--- --- ---')

    '''测量10000个key value的简单数值map传递耗时'''
    param = HashMap()
    num = 1
    for i in range(10000):
        param.put(num, num)
        num = num + 2
    start = time.time()
    result = test2.testMap3(param)
    end = time.time()
    print(end - start)
    print((end - start) * 1000)
    print(result.size())
    print('--- --- ---')

    '''测量10000个element的简单数值list传递耗时'''
    param = ArrayList()
    num = 1
    for i in range(10000):
        param.add(num)
        num = num + 2
    start = time.time()
    result = test2.testList3(param)
    end = time.time()
    print(end - start)
    print((end - start) * 1000)
    print(result.size())
    print('--- --- ---')

    '''测量100个复杂对象map传递耗时'''
    param = HashMap()
    num = 1
    for i in range(100):
        object = buildComplexObject()
        param.put(num, object)
        num = num + 2
    start = time.time()
    result = test2.testMap4(param)
    end = time.time()
    print(end - start)
    print((end - start) * 1000)
    print(result.size())
    print('--- --- ---')

    '''测量100个复杂对象list传递耗时'''
    param = ArrayList()
    for i in range(100):
        object = buildComplexObject()
        param.add(object)
    start = time.time()
    result = test2.testList4(param)
    end = time.time()
    print(end - start)
    print((end - start) * 1000)
    print(result.size())
    print('--- --- ---')


    jpype.shutdownJVM()
