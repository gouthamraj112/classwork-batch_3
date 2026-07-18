class DevConfig:
    database="aqlite.db"
    debug=True
class TestConfig:
    database="test.db"
    debug=True
class ProdConfig:
    database="mysql://food_app"
    debug=False

def get_config(environment):
    if environment=="dev":
        return DevConfig()
    elif environment=="test":
        return TestConfig()
    else:
        return ProdConfig()
    
env="dev"
config=get_config(env)

print(config.database)
print(config.debug)
 
 
    
