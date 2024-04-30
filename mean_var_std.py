import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list)
        a = a.reshape(3, 3)

        mean_axis1 = np.mean(a, axis=0).tolist()
        mean_axis2 = np.mean(a, axis=1).tolist()
        mean_flat = np.mean(a).tolist()

        var_axis1 = np.var(a, axis=0).tolist()
        var_axis2 = np.var(a, axis=1).tolist()
        var_flat = np.var(a).tolist()

        std_axis1 = np.std(a, axis=0).tolist()
        std_axis2 = np.std(a, axis=1).tolist()
        std_flat = np.std(a).tolist()

        max_axis1 = np.max(a, axis=0).tolist()
        max_axis2 = np.max(a, axis=1).tolist()
        max_flat = np.max(a).tolist()

        min_axis1 = np.min(a, axis=0).tolist()
        min_axis2 = np.min(a, axis=1).tolist()
        min_flat = np.min(a).tolist()

        sum_axis1 = np.sum(a, axis=0).tolist()
        sum_axis2 = np.sum(a, axis=1).tolist()
        sum_flat = np.sum(a).tolist()
   

    calculations = { 
        'mean' : [mean_axis1,mean_axis2,mean_flat],
        'variance' : [var_axis1,var_axis2,var_flat],
        'standard deviation' : [std_axis1,std_axis2,std_flat],
        'max':[max_axis1,max_axis2, max_flat],
        'min':[min_axis1, min_axis2, min_flat],
        'sum':[sum_axis1, sum_axis2, sum_flat]
    }


    return calculations