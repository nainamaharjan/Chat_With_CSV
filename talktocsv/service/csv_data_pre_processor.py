"""
   Created by: Naina Maharjan
   Created on: 2024-07-27
"""
from typing import List, Any
from settings import ROWS_TO_ADD
def died(x):
    if x == '9999-99-99':
        return 0
    else:
        return 1

sex_map = {1: 'Male', 2: 'Female'}
patient_type_map = {1: 'Outpatient', 2: 'Inpatient'}
intubed_map = {1: 'Yes', 2: 'No'}
pneumonia_map = {1: 'Yes', 2: 'No'}
pregnant_map = {1: 'Yes', 2: 'No'}
condition_map = {1: 'Yes', 2: 'No'}
classification_map = {1: 'Not a case', 2: 'Suspected', 3: 'Confirmed', 5: 'Confirmed', 7: 'Confirmed'}
icu_map = {1: 'Yes', 2: 'No'}

# Applying mappings

def apply_map(df):
    df['SEX'] = df['SEX'].map(sex_map)
    df['PATIENT_TYPE'] = df['PATIENT_TYPE'].map(patient_type_map)
    df['INTUBED'] = df['INTUBED'].map(intubed_map)
    df['PNEUMONIA'] = df['PNEUMONIA'].map(pneumonia_map)
    df['PREGNANT'] = df['PREGNANT'].map(pregnant_map)
    df['DIABETES'] = df['DIABETES'].map(condition_map)
    df['COPD'] = df['COPD'].map(condition_map)
    df['ASTHMA'] = df['ASTHMA'].map(condition_map)
    df['INMSUPR'] = df['INMSUPR'].map(condition_map)
    df['HIPERTENSION'] = df['HIPERTENSION'].map(condition_map)
    df['OTHER_DISEASE'] = df['OTHER_DISEASE'].map(condition_map)
    df['CARDIOVASCULAR'] = df['CARDIOVASCULAR'].map(condition_map)
    df['OBESITY'] = df['OBESITY'].map(condition_map)
    df['RENAL_CHRONIC'] = df['RENAL_CHRONIC'].map(condition_map)
    df['TOBACCO'] = df['TOBACCO'].map(condition_map)
    df['CLASIFFICATION_FINAL'] = df['CLASIFFICATION_FINAL'].map(classification_map)
    df['ICU'] = df['ICU'].map(icu_map)
    df['DEATH'] = df['DEATH'].map(icu_map)
    df['Covid'] = df['Covid'].map(icu_map)
    return df

# Function to create a sentence from a row
def row_to_sentence(row):
    return (f"A {row['AGE']} year old {row['SEX']} patient, classified as {row['CLASIFFICATION_FINAL']}, "
            f"was treated as an {row['PATIENT_TYPE']}. "
            f"Intubated: {row['INTUBED']}. Pneumonia: {row['PNEUMONIA']}. "
            f"Diabetes: {row['DIABETES']}. COPD: {row['COPD']}. Asthma: {row['ASTHMA']}. "
            f"Immunosuppressed: {row['INMSUPR']}. Hypertension: {row['HIPERTENSION']}. Other diseases: {row['OTHER_DISEASE']}. "
            f"Cardiovascular diseases: {row['CARDIOVASCULAR']}. Obesity: {row['OBESITY']}. "
            f"Chronic renal disease: {row['RENAL_CHRONIC']}. Tobacco use: {row['TOBACCO']}. "
            f"Pregnant: {row['PREGNANT']}. ICU: {row['ICU']}. Death: {row['DEATH']}. Covid: {row['Covid']}.")




def convert_df_to_contextual_sentences(df,df_only=False)->Any:
    print("Preparing data")
    df_copy = df.copy()
    df_copy['DEATH'] = df_copy['DATE_DIED'].apply(died)
    df_copy.drop(columns=['DATE_DIED'], inplace=True)
    df_copy['Covid'] = df_copy['CLASIFFICATION_FINAL'].apply(lambda x: 0 if x >= 4 else 1)
    df_copy['PREGNANT'] = df_copy['PREGNANT'].replace({97: 2, 98: 0})
    df_copy['ICU'] = df_copy['ICU'].replace({97: 2, 99: 0})
    df_copy['INTUBED'] = df_copy['INTUBED'].replace({97: 2})
    df_copy = apply_map(df_copy)
    df_10000 = df_copy.sample(n=ROWS_TO_ADD, random_state=1)
    if df_only:
        return df_copy
    print(type(df_10000))
    sentences = df_10000.apply(row_to_sentence, axis=1).to_list()
    ids = [str(i) for i in list(range(1, ROWS_TO_ADD+1))]
    print("preprocessing data complete")
    return sentences, ids, df_10000