import pandas as pd
## create family excel 

df = pd.DataFrame([],
    columns = 
    [
    'familyname',
    'familyid',
    'username',
    'userid',
    'resources',
    'influence',
    'manpower',
    'mana',
    'keywords'
    ])
df.to_csv('family.csv')


df = pd.DataFrame([],
    columns = 
    [
    'familyid',
    'charid',
    'charname',
    'charage',
    'position',
    'positionid',
    'conditions',
    'prestige',
    'might',
    'authority',
    'stewardship',
    'cunning',
    'presence',
    'knowledge',
    'intellect'
    ])
df.to_csv('family_members.csv')


df = pd.DataFrame([],
    columns = 
    [
    'familyid',
    'estateid',
    'provienceid',
    'estatename',
    'estatetype',
    'goodstype'
    'size',
    'c_resources',
    'c_influence',
    'c_manpower',
    'c_mana'
    ])
df.to_csv('estate.csv')

# provinces 
df = pd.DataFrame([],
    columns = 
    [
    'provienceid',
    'proviencename',
    'proviencesize',
    'proviencepop',
    'poptype1',
    'poptype2'
    'poptype3'
    ])
df.to_csv('provinces.csv')
# positions
df = pd.DataFrame([],
    columns = 
    [
    'positionid',
    'actionid',
    'charid',
    'positionname',
    'voteregularity',
    'nextvote',
    'votetype',
    'seniority'
    ])

df.to_csv('positions.csv')


# actions
df = pd.DataFrame([],
    columns = 
    [
    'actionid',
    'actionname',
    'descriptions',
    'cost',
    'avalibile_roles'
    ])



# position history
df = pd.DataFrame([],
    columns = 
    [
    'positionid',
    'charid',
    'turn',
    'positionname',
    'seniority'

    ])
df.to_csv('position_history.csv')
# vote_proposal
#
df = pd.DataFrame([],
    columns = 
    [
    'proposalid',
    'charid',
    'familyid',
    'votetype',
    'proposaltext'
    ])
df.to_csv('vote_proposal.csv')

# votes

df = pd.DataFrame([],
    columns = 
    [
    'proposalid',
    'charid',
    'familyid',
    'votetype',
    'voteid',
    'voteweight'
    ])
df.to_csv('vote_proposal.csv')

