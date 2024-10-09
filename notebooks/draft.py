import os
project_root = os.path.dirname(os.path.dirname(__file__))
print(project_root)
print(os.path.dirname(__file__))

FP_rad = 2
FP_len = 1024
print(os.path.join(project_root, 'models', 'full_reaxys_model_1024bool', 'model.ckpt-10654.as_numpy.pickle'), FP_rad=FP_rad, FP_len=FP_len)

#line 103 standalone_model_num
#fid = fid.decode('utf-8')