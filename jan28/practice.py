import sqlite3
import pandas as pd


def hr_phillies_list():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()

    query = """
        SELECT yearID, sum(HR)
        FROM batting
        WHERE teamID = 'PHI'
        GROUP BY yearID
        
    
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns = ['yearID', 'sum(HR)'])
    print(df)
    

def teams_in_25():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    
    query = """
        SELECT teamID, sum(HR)
        FROM batting
        WHERE yearID = 2025
        GROUP BY teamID
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close
    
    df = pd.DataFrame(records, columns = ['teamID', 'sum(HR)'])
    
    print(df)
    


def most_HR_players():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    
    query = """
        SELECT playerID, sum(HR)
        FROM batting
        GROUP BY playerID
        ORDER BY sum(HR) DESC
        LIMIT 10
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns = ['playerID', 'sum(HR)'])
    
    print(df)
    

def years_list_HR_PHI():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    
    query = """
        SELECT yearID, sum(HR)
        FROM batting
        WHERE teamID = 'PHI'
        GROUP BY yearID
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns = ['yearID', 'sum(HR)'])
    print(df)
    


def teams_over200_HR():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    
    query = """
        SELECT teamID, sum(HR)
        FROM batting
        WHERE yearID = 2025
        GROUP BY teamID
        HAVING sum(HR) >= 200
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns = ['teamID', 'sum(HR)'])
    
    print(df)
    
    

def baberuth_infor():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    
    query = """
        SELECT batting.yearID, name, batting.HR
        FROM batting INNER JOIN teams
        ON batting.teamID = teams.teamID AND batting.yearID = teams.yearID
        WHERE playerID = 'ruthba01'
    """
    
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns = ['yearID', 'name', 'HR'])
    
    print(df)
    


def over_2_teams():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    
    query = """
        SELECT playerID, count(*)
        FROM batting
        WHERE yearID = 1976
        GROUP BY teamID
        HAVING count(*) >= 2
    
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns = ['playerID', 'count(*)'])
    print(df)
    
over_2_teams()
    
    