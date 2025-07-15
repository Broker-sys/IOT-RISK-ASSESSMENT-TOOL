import pandas as pd # type: ignore

def iot_security_risk_assessment(data):


    # Normalizing string values to ensure consistent comparison
    data['Connectivity'] = data['Connectivity'].str.capitalize()
    data['Data Sensitivity'] = data['Data Sensitivity'].str.capitalize()
    data['Authentication'] = data['Authentication'].str.capitalize()
    data['Software Updates'] = data['Software Updates'].str.capitalize()

    # Initialiazing all risk levels to Medium
    data['Risk Level'] = 'Medium'

    # Applying rules for high risk
    data.loc[data['Connectivity'] == 'Public', 'Risk Level'] = 'High'
    data.loc[data['Data Sensitivity'] == 'High', 'Risk Level'] = 'High'
    data.loc[data['Authentication'] == 'None', 'Risk Level'] = 'High'
    data.loc[data['Software Updates'] == 'Outdated', 'Risk Level'] = 'High'

    # Applying rules for low risk
    data.loc[data['Authentication'] == 'Stable', 'Risk Level'] = 'Low'
    data.loc[data['Software Updates'] == 'Frequent', 'Risk Level'] = 'Low'

    return data
data = {
    'Device Name': ['Smart fingerprint', 'Smart Camera', 'Smart Door Lock'],
    'IP Address': ['192.158.1.102', '192.168.1.101', '192.168.1.102'],
    'Connectivity': ['Private', 'Public', 'Public'],
    'Data Sensitivity': ['Weak', 'Medium', 'Weak'],
    'Authentication': ['Weak', 'Medium', 'Weak'],
    'Software Updates': ['Outdated', 'frequent', 'Frequent']
}

df = pd.DataFrame(data)

assessed_df = iot_security_risk_assessment(df)
assessed_df