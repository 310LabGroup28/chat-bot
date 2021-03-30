import unittest
import HTMLReport


from geoInfo import GeoInfo as gi
from witapi import WitAPI as wa
from location import Location as lc
from timechatbot import TimeChatbot as tc

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 1.
        print ("this setupclass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        # 4.
        print ("this teardownclass() method only called once too.\n")

    def setUp(self):
        # 2.
        print ("do something before test : prepare environment.\n")

    def tearDown(self):
        # 3.
        print ("do something after test : clean up.\n")

    def test_location(self):
        # test getLocation method
        L1 = lc.getLocation('here')
        L2 = lc.getLocation('me')
        L3 = lc.getLocation()
        self.assertEqual(L1, L2)
        self.assertEqual(L1, L3)
        L4 = lc.getLocation('New York')
        new_york = (40.7127281, -74.0060152)
        self.assertEqual(new_york, L4)
        toronto = (43.6534817, -79.3839347)
        L5 = lc.getLocation('Toronto')
        self.assertEqual(toronto, L5)
        # test distanceByLatLong
        question = 'distance from London to Toronto'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        d1 = lc.distanceByLatLong(entities)
        question = 'how far it is from Toronto to London'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        d2 = lc.distanceByLatLong(entities)
        self.assertEqual(d1, d2)
        #print(d1, d2, entities)

    def test_geoInfo(self):
        # test get_temperature
        question = 'temperature in London'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        t1 = gi.get_temperature(entities)
        question = 'London temperature'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        t2 = gi.get_temperature(entities)
        self.assertEqual(t1, t2)
        #print(t1, t2)
        # test get_weather
        question = 'how about the weather in Toronto'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        w1 = gi.get_weather(entities)
        question = 'what is the weather of Toronto'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        w2 = gi.get_weather(entities)        
        self.assertEqual(w1, w2)
        #print(w1, w2)        
        # test get_point_of_interest
        question = 'what is the point of interest in Washington'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        poi1 = gi.get_point_of_interest(entities, limit=6)        
        self.assertEqual(6, len(poi1))
        #print(poi1)

    def test_timeChatbot(self):
        # test getTimezone
        question = 'what is the time in Toronto'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        [t1] = tc.getTimezone(entities)
        t2 = tc.getTimezone({}, 'Toronto')        
        self.assertEqual(t1, t2)
        #print(t1, t2)
        # test getLocalTime
        [lt1] = tc.getLocalTime(entities)
        question = 'the local time of Toronto'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        lt2 = tc.getLocalTime(entities, 'Toronto')
        # their seconds may be a little different, because of time lag
        # but, generally speaking, their dates, hours and minutes should be the same
        lt1 = str(lt1)[:16]
        lt2 = str(lt2)[:16]
        self.assertEqual(lt1, lt2)
        # test getTimeDifference
        question = 'the time difference between London and Toronto'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        td1 = tc.getTimeDifference(entities)
        question = 'the time difference between Toronto and London'
        jsonData = wa.sendRequest(question)
        entities = jsonData['entities']
        td2 = tc.getTimeDifference(entities)
        td1 = str(td1)[:16]
        td2 = str(td2)[:16]
        #print(td1, td2)
        self.assertEqual(td1, td2)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((loader.loadTestsFromTestCase(TestDemo)))
    # set the runner
    runner = HTMLReport.TestRunner(report_file_name='test',
                                   output_path='report',
                                   title='testing report',
                                   description='desc of report',
                                   sequential_execution=True, 
                                   lang='en'
                                   )
    # run the suite
    runner.run(suite)
