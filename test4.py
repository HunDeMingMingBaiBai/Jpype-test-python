import time
import jnius_config
#jvmArg = '-Djava.class.path=/Users/4paradigm/IdeaProjects/Jpype-test/out/artifacts/Jpype_test_jar/Jpype-test.jar'
#jnius_config.add_options(jvmArg)
jnius_config.set_classpath('.', '/Users/4paradigm/IdeaProjects/Jpype-test/out/artifacts/Jpype_test_jar/Jpype-test.jar')
from jnius import autoclass

if __name__ == '__main__':
    Test1 = autoclass("com.paradigm.jpype.Test1")
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
    Test2 = autoclass('com.paradigm.jpype.Test2')
    Data = autoclass('com.paradigm.jpype.Data')
    HashMap = autoclass("java.util.HashMap")
    ArrayList = autoclass("java.util.ArrayList")
    Integer = autoclass("java.lang.Integer")
    Double = autoclass("java.lang.Double")
    param = HashMap()
    list = ArrayList()
    list.add(1)
    list.add(3)
    list.add(5)
    data = Data()
    data.setData("hello data 1")
    test2 = Test2()
    param.put("int", Integer(1))
    param.put("double", Double(1.0))
    param.put("list", list)
    param.put("str", "hello1")
    param.put("data", data)
    result = test2.testMap(param)
    print(result.toString())
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
    list.add(Double(1.0))
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
    print(resultList.toString())
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
    ComplexObject = autoclass("com.paradigm.jpype.ComplexObject")
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
    print(resultObject.toString())
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