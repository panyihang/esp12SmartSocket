class cpu():
    def cpuFrep(LOW_OR_HIGH):
        import machine
        if LOW_OR_HIGH == 'LOW' or LOW_OR_HIGH == 'low' or LOW_OR_HIGH == 'Low' or LOW_OR_HIGH == 0:
            if int(machine.freq()) == 80000000:
                pass
            else:
                machine.freq(80000000)
                print('now cpu freq is %s' % int(machine.freq()))
        if LOW_OR_HIGH == 'HIGH' or LOW_OR_HIGH == 'high' or LOW_OR_HIGH == 'High' or LOW_OR_HIGH == 1:
            if int(machine.freq()) == 160000000:
                pass
            else:
                machine.freq(160000000)
                print('now cpu freq is %s' % int(machine.freq()))
        else:
            return('INPUT_INFO_ERROR')

    def getCPUFreq():
        import machine
        return(machine.freq())
