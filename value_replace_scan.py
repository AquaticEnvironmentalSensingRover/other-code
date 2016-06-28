def valueReplaceScan(value):
    if type(value) == type(list()):
        for ii in range(len(value)):
            value[ii] = valueReplaceScan(value[ii])
    
    elif not value == None:
            value = "Ok"
    
    return value

if __name__ == "__main__":
    print valueReplaceScan([None,[1,1],[None,[None,3],None], object])
    print valueReplaceScan(None)
    print valueReplaceScan(object)