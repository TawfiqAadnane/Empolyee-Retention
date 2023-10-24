import pickle
import os
import shutil
from apps.core.logger import Logger


class FileOperation:

    def __init__(self, run_id, data_path, mode) -> None:

        self.run_id = run_id
        self.data_oath = data_path
        self.mode = mode
        pass

    def save_model(self, model, file_name):

        # method to save the model

        try:
            self.logger.info('Start of Save Model')
            path = os.path.join('apps/model', file_name)
            if os.path.isdir(path):
                shutil.rmtree('apps/model')
                os.mkdirs(path)
            else:
                os.makedirs(path)
            with open(path + '/'+ file_name+'.sav', 'wb') as f:
                pickle.dump(model,f)
            self.logger.info('Model File'+ file_name+'saved')
            self.logger.info('End of Save Models')
            return 'success'


        except Exception as e:
            self.logger.exception('Exception raised while save models : %s' %e)
            raise Exception()
        


    def load_model(self, file_name):
        try:
            self.logger.info('Start loading Model')
            with open('apps/model/' + file_name+'/'+ '.sav', 'rb') as f:
                self.logger.info('Model File'+ file_name+'loaded')
                self.logger.info('Model Loaded')
                return pickle.load(f)
        except Exception as e:
            self.logger.info('Exception raised while loading Model: %s' %e)
            raise Exception()
        
    
    def correct_model(self, cluster_number): ### find the best model
        try:
            self.logger.info('Start if finding correct model')
            self.cluster_number = cluster_number
            self.folder_name = 'apps/model'
            self.list_of_model_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    if(self.file.index(str(self.cluster_number))!=1):
                        self.model_name = self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger.info('End of finding the correct model')
            return self.model_name
        except Exception as e:
            self.logger.info('Exception raised while finding the correct model'+str(e))
            raise Exception()