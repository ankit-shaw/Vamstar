import pandas as pd
import sys


def createDataFrame(file_Path):
    data_frame = pd.read_json(file_Path)
    return data_frame


def createBMI( data_frame ):
    data_frame = data_frame.assign(BMI=lambda x: x.WeightKg / ((x.HeightCm * 0.01) ** 2))
    return data_frame


def createRisk_Category(data_frame):

    data_frame['BMI Category'] = [
        'Underweight' if x < 18.5 else 'Normal weight'
        if x < 25 else 'Overweight' if x < 30 else 'Moderately Obese'
        if x < 35 else 'Severly Obese' if x < 40 else 'Very severly Obese'
        for x in df.BMI]

    data_frame['Health Risk'] = [
        'Malnutrition' if x < 18.5 else 'Low risk'
        if x < 25 else 'Enhanced risk' if x < 30 else 'Medium risk'
        if x < 35 else 'Hish risk' if x < 40 else 'Very high risk'
        for x in df.BMI]

    return data_frame


if __name__ == "__main__":
    file_path = input('insert file path : ')
    # file_path = print("input the file path: ", sys.argv[0])

    # creating Data Frame
    df = createDataFrame(file_path)

    # adding BMI index to existing Data Frame
    df = createBMI(df)

    '''adding BMI Category and Health risk with respect
     to BMI index in the current Data Frame'''
    df = createRisk_Category(data_frame=df)
    print(df)
