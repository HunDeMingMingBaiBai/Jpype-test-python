import time
import jnius_config
import logging
#jvmArg = '-Djava.class.path=/Users/4paradigm/IdeaProjects/Jpype-test/out/artifacts/Jpype_test_jar/Jpype-test.jar'
#jnius_config.add_options(jvmArg)
jnius_config.set_classpath('.', '/Users/4paradigm/IdeaProjects/Jpype-test/out/artifacts/Jpype_test_jar/Jpype-test.jar')
jnius_config.set_classpath('.', '/home/yuxiaojie/test-hide/Jpype-java.jar')
from jnius import autoclass

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
    logging.basicConfig(level=logging.INFO)
    while True:
        Test1 = autoclass("com.paradigm.jpype.Test1")
        test = Test1()
        for i in range(10):
            start = time.time()
            result = test.run1(100000)
            end = time.time()
            logging.info('--- --- ---')
            logging.info(result)
            logging.info(end - start)
            logging.info((end - start) * 1000)
            logging.info('--- --- ---')

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
        logging.info(result.toString())
        logging.info(result.get("int"))
        logging.info(result.get("double"))
        resultList = result.get("list")
        logging.info("list start")
        for i in resultList:
            logging.info(i)
        logging.info("list end")
        resultData = result.get("data")
        logging.info(resultData.getData())
        logging.info('--- --- ---')

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
        logging.info(resultList.toString())
        logging.info(resultList[0])
        logging.info(resultList[1])
        logging.info(resultList[2])
        logging.info("list start")
        for i in resultList[3]:
            logging.info(i)
        logging.info("list end")
        logging.info("map start")
        for entry in resultList[4].entrySet():
            logging.info(entry.getKey() + " : " + str(entry.getValue()))
        logging.info("map end")
        resultData = resultList[5]
        logging.info(resultData.getData())
        logging.info('--- --- ---')

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
        logging.info(resultObject.toString())
        logging.info(resultObject.getIntValue())
        logging.info(resultObject.getLongValue())
        logging.info(resultObject.getDoubleValue())
        logging.info(resultObject.getStr())
        logging.info("list start")
        for i in resultObject.getList():
            logging.info(i)
        logging.info("list end")
        logging.info("map start")
        for entry in resultObject.getMap().entrySet():
            logging.info(entry.getKey() + " : " + str(entry.getValue()))
        logging.info("map end")
        resultData = resultObject.getData()
        logging.info(resultData.getData())
        logging.info('--- --- ---')

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
        logging.info(result.toString())
        logging.info("list start")
        for i in result.get("list"):
            logging.info(i)
        logging.info("list end")
        logging.info("map start")
        for entry in result.get("map").entrySet():
            logging.info(entry.getKey() + " : " + str(entry.getValue()))
        logging.info("map end")
        logging.info(result.get("object").toString())
        logging.info('--- --- ---')

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
        logging.info(result.toString())
        logging.info("map start")
        for entry in result.get(0).entrySet():
            logging.info(entry.getKey() + " : " + str(entry.getValue()))
        logging.info("map end")
        logging.info("list start")
        for i in result.get(1):
            logging.info(i)
        logging.info("list end")
        logging.info(result.get(2).toString())
        logging.info('--- --- ---')

        '''测量10000个key value的简单数值map传递耗时'''
        param = HashMap()
        num = 1
        for i in range(10000):
            param.put(num, num)
            num = num + 2
        start = time.time()
        result = test2.testMap3(param)
        end = time.time()
        logging.info(end - start)
        logging.info((end - start) * 1000)
        logging.info(result.size())
        logging.info('--- --- ---')

        '''测量10000个element的简单数值list传递耗时'''
        param = ArrayList()
        num = 1
        for i in range(10000):
            param.add(num)
            num = num + 2
        start = time.time()
        result = test2.testList3(param)
        end = time.time()
        logging.info(end - start)
        logging.info((end - start) * 1000)
        logging.info(result.size())
        logging.info('--- --- ---')

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
        logging.info(end - start)
        logging.info((end - start) * 1000)
        logging.info(result.size())
        logging.info('--- --- ---')

        '''测量100个复杂对象list传递耗时'''
        param = ArrayList()
        for i in range(100):
            object = buildComplexObject()
            param.add(object)
        start = time.time()
        result = test2.testList4(param)
        end = time.time()
        logging.info(end - start)
        logging.info((end - start) * 1000)
        logging.info(result.size())
        logging.info('--- --- ---')

        time.sleep(5)

