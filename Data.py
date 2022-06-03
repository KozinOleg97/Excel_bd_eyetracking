import numpy as np
import pandas as pd

mainDataList = []

for i in range(59):
    list = []
    mainDataList.append(list)

indexDataList = []

mainDataFrameCorsi = pd.DataFrame(
    columns=['Slides_Mean', 'Duration blinks - Max (ms)_Mean', 'Duration blinks - Min (ms)_Mean',
             'Duration blinks - Average (ms)_Mean', 'Duration blinks - Std (ms)_Mean', 'Number blinks_Mean',
             'Frequency blinks (number/s)_Mean', 'Duration fixations - Max (ms)_Mean',
             'Duration fixations - Min (ms)_Mean', 'Duration fixations - Average (ms)_Mean',
             'Duration fixations - Std (ms)_Mean', 'Diameter pupil fixations - Max_Mean',
             'Diameter pupil fixations - Min_Mean', 'Diameter pupil fixations - Average_Mean',
             'Diameter pupil fixations - Std_Mean', 'Number fixations_Mean', 'Number fixations in question_Mean',
             'Number fixations rereading_Mean', 'Frequency fixation (number/s)_Mean', 'Time first fixation (ms)_Mean',
             'Deviation area_Mean', 'Diameter pupil - Max_Mean', 'Diameter pupil - Min_Mean',
             'Diameter pupil - Average_Mean', 'Diameter pupil - Std_Mean', 'Areas under PD_Mean',
             'Browsing speed (pixels/ms)_Mean', 'Sum areas_Mean', 'Time in slide (ms)_Mean',
             'Percent validation (%)_Mean', 'Slides_SD', 'Duration blinks - Max (ms)_SD',
             'Duration blinks - Min (ms)_SD', 'Duration blinks - Average (ms)_SD', 'Duration blinks - Std (ms)_SD',
             'Number blinks_SD', 'Frequency blinks (number/s)_SD', 'Duration fixations - Max (ms)_SD',
             'Duration fixations - Min (ms)_SD', 'Duration fixations - Average (ms)_SD',
             'Duration fixations - Std (ms)_SD', 'Diameter pupil fixations - Max_SD',
             'Diameter pupil fixations - Min_SD', 'Diameter pupil fixations - Average_SD',
             'Diameter pupil fixations - Std_SD', 'Number fixations_SD', 'Number fixations in question_SD',
             'Number fixations rereading_SD', 'Frequency fixation (number/s)_SD', 'Time first fixation (ms)_SD',
             'Deviation area_SD', 'Diameter pupil - Max_SD', 'Diameter pupil - Min_SD', 'Diameter pupil - Average_SD',
             'Diameter pupil - Std_SD', 'Areas under PD_SD', 'Browsing speed (pixels/ms)_SD', 'Sum areas_SD',
             'Time in slide (ms)_SD', 'Percent validation (%)_SD'
             ])

indexDataFrame = pd.DataFrame(columns=['Index'])
