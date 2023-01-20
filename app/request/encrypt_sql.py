from cryptography.fernet import Fernet

key=''
username=b'gAAAAABjySFR6_p8bwpVoks3ibm-k8QDCnb-IH02nNKj0Hk1Sd--wW_SVCYKF_ZI1hDOpDwVzsdY5WmDBynA=='
password=b'gAAAAABjySFRquTjDSbWAq97r3lpFFv9xDXLuX7Ne1xnW-kXYs_T3p_aWu5qc24oDqYxetqsOXXfYWXQ=='
server=b'gAAAAABjySFwrUq_zlHqfhriVkDrCQcf2YRDiaVoVfJ2rmu08jOeVSIZOHg4pbJGeVUjZwMCny-cinY99Q=='
database=b'gAAASFRqRE9F89rWMJIispAImxGz7ABPe4t9o2gINW4fYVbwDh95hkTk1vyJV55F_uCiM1yh7A4LEzuPmsti1m3wMZcHCN2uifsg='
connect=b'ABjySj8JvtHINpKZLBRDhTxGLv9y_U4ynX3LtNJyANICJgZpx-19HTdgs1CZOOmF-4ay8j3XsfwJ4PM1OuJRWPu7RKnCJCp8Q4PRqpAfLq7hX0b9oOPmrl051rvR'

fernet = Fernet(key)
server = fernet.decrypt(server).decode()
username = fernet.decrypt(username).decode()
password= fernet.decrypt(password).decode()
database = fernet.decrypt(database).decode()
connect = fernet.decrypt(connect).decode()






