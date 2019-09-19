from datetime import datetime, date, timedelta
import os


class Cats:
    def __init__(self):
        self.now = datetime.now()

    def main(self):

        if os.path.isfile("cats_time.txt"):
            stat = os.stat("cats_time.txt")
            cat_file_modified_date = date.fromtimestamp(stat.st_mtime)
            if date.today() == cat_file_modified_date:
                arrival_time = self.get_arrival_time()
            else:
                arrival_time = self.enter_arrival_time()
        else:
            arrival_time = self.enter_arrival_time()

        arrival_hour, arrival_min, tot_working_hour_after_deduction = self.calculate_working_hours(arrival_time)

        print "#" * 90
        print "Total hours after deduction: ", tot_working_hour_after_deduction
        print "plus/minus: ", tot_working_hour_after_deduction - 7.8

        expected_departure = ((int(arrival_hour) + 7) * 100 + 100 * (int(arrival_min) + 80) / 60) / 100 + 0.5
        best_departure = ((int(arrival_hour) + 8) * 100 + 100 * (int(arrival_min) + 80) / 60) / 100
        print "Expected departure time :", expected_departure
        print "Optimal departure time :", best_departure
        print "#" * 90

    def calculate_working_hours(self, arrival_time):
        departure_hour = self.now.strftime("%H")
        departure_min = self.now.strftime("%M")
        arrival_hour = arrival_time.split(':')[0]
        arrival_min = arrival_time.split(':')[1]

        worked_hour = int(departure_hour) - int(arrival_hour)
        worked_min = int(departure_min) - int(arrival_min)
        tot_working_hour = (worked_hour * 100 + 100 * worked_min / 60) / 100
        if tot_working_hour > 9.5:
            tot_working_hour_after_deduction = tot_working_hour - 0.75
        elif tot_working_hour > 6:
            tot_working_hour_after_deduction = tot_working_hour - 0.5
        else:
            tot_working_hour_after_deduction = tot_working_hour
        return arrival_hour, arrival_min, tot_working_hour_after_deduction


    def get_arrival_time(self):
        file1 = open("cats_time.txt", "r+")
        arrival_time = file1.read()
        print arrival_time
        return
        print "Today's arrival time is ", str(arrival_time)
        return self.now.replace(hour=int(arrival_time.split(':')[0]), minute=int(arrival_time.split(':')[1]),second=00)

    def enter_arrival_time(self):
        file1 = open("cats_time.txt", "w")
        arrival_time = raw_input("Enter today's arrival time (example 8:30) :")
        file1.write(arrival_time)
        file1.close()
        return self.now.replace(hour=int(arrival_time.split(':')[0]), minute=int(arrival_time.split(':')[1]),second=00)

    def sample_test_data(self):
        dict1={
            1:[datetime.strptime('09/19/18 9:25','%m/%d/%y %H:%M'), datetime.strptime("09/19/18 18:37",'%m/%d/%y %H:%M')],
            2:[datetime.strptime('09/19/18 10:16','%m/%d/%y %H:%M'),datetime.strptime("09/19/18 18:51",'%m/%d/%y %H:%M')],
            3:[datetime.strptime('09/19/18 10:48','%m/%d/%y %H:%M'),datetime.strptime("09/19/18 18:44",'%m/%d/%y %H:%M')],
            4:[datetime.strptime('09/19/18 08:55','%m/%d/%y %H:%M'),datetime.strptime("09/19/18 18:48",'%m/%d/%y %H:%M')]
        }
        print  "{:^19}  {:^19}  {:^6}  {:^6}  {:^6}  {:^6}".format("from", "to", "Hrs", "Work Hr", "Plnd", "Flex")
        print "{:72}".format("-"*72)

        for k,v in dict1.iteritems():
            Hrs = float(int(str(v[1]-v[0]).split(':')[0])*100+int(str(v[1]-v[0]).split(':')[1])*100/60)/100
            if Hrs>9:
                Working_hour=Hrs-0.75
            elif Hrs>6:
                Working_hour=Hrs-0.5
            else:
                Working_hour=Hrs
            Plnd=7.8
            Flex=Working_hour-Plnd
            print  "{:^19}  {:^19}  {:>6}  {:>6}  {:>6}  {:>6}".format(str(v[0]),str(v[1]),str(Hrs),str(Working_hour),str(Plnd),str(Flex))

    def cal_expected_time(self):
        at=self.get_arrival_time()
        #at=self.enter_arrival_time()
        #print at
        #print self.now
        #Hrs = float(int(str(self.now-at).split(':')[0])*100+int(str(self.now-at).split(':')[1])*100/60)/100
        #print Hrs
        print "-"*200

        exp_wh=timedelta(hours=7, minutes=48)
        break_30_min=timedelta(minutes=30)
        break_45_min=timedelta(minutes=45)
        print exp_wh
        #print datetime.datetime.

        return



        #if total working hours less than 9.30 hours, then 0.30 min will be the break
        print "Your departure time today is {}. And your flex time is {} ".format((at + timedelta(hours=7, minutes=48)+timedelta(minutes=30)).strftime('%H:%M'),0)
        #if total working hours exceed 9.30 then 0.45 min will be the break
        print "Best departure time today {}. And your flex time is {} ".format((at + timedelta(hours=8, minutes=59)+timedelta(minutes=30)).strftime('%H:%M'),float(111*100/60)/100)
        print "Max departure time today {}. And your flex time is {}".format((at + timedelta(hours=9, minutes=15)+timedelta(minutes=45)).strftime('%H:%M'),float(127/60))
        print "-"*200
    def test1(self):
        print range(0,15,5)
        mygenerator=(x*x for x in range(15))
        for i in mygenerator:
            print i

    def createGenerator(self):
        mylist=range(5)
        for i in mylist:
            yield i*i

    def test3_learning_fork(self):
        print "hello world"
        import os

        def child():
            print('\nA new child ',  os.getpid())
            os._exit(0)

        def parent():
            while True:
                newpid = os.fork()
                if newpid == 0:
                    child()
                else:
                    pids = (os.getpid(), newpid)
                    print("parent: %d, child: %d\n" % pids)
                reply = raw_input("q for quit / c for new fork")
                if reply == 'c':
                    continue
                else:
                    break

        parent()



    def test2(self):
        mygen=self.createGenerator()
        print mygen
        for i in mygen:
            print i

    def test5_learn_about_pipes(self):
        import os, time, sys
        pipe_name = 'pipe_test'

        def child( ):
            pipeout = os.open(pipe_name, os.O_WRONLY)
            counter = 0
            while True:
                time.sleep(1)
                os.write(pipeout, 'Number %03d\n' % counter)
                counter = (counter+1) % 5

        def parent( ):
            pipein = open(pipe_name, 'r')
            while True:
                line = pipein.readline()[:-1]
                print 'Parent %d got "%s" at %s' % (os.getpid(), line, time.time( ))

        if not os.path.exists(pipe_name):
            os.mkfifo(pipe_name)
        pid = os.fork()
        if pid != 0:
            parent()
        else:
            child()

if __name__ == '__main__':
    #Cats().cal_expected_time()
    #Cats().test3()
    #from cross_system_setup_e14 import loadPreviousDateStlPrices
    #loadPreviousDateStlPrices()
    #Cats().test3_learning_fork()
    Cats().test5_learn_about_pipes()
