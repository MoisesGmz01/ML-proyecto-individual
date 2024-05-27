import pandas as pd

dataset=pd.read_parquet(r'C:\Users\Moises\Desktop\Projecto invidual 1\archivos limpios\data_final.parquet')
df_developer=pd.read_parquet(r'C:\Users\Moises\Desktop\Projecto invidual 1\archivos limpios\games.parquet')

#Funcion 1
df_1=df_developer[['developer','release_date','price','title']]
df_1=df_1.drop_duplicates(subset=['developer','title']).copy()

def developer_info(developer: str):
    df=df_1[df_1['developer']==developer]
    if developer not in list(df_1['developer']):
        return {'El desarrollador no se encuentra en la base de datos'}
    else:
        fechas=df['release_date'].unique()
        anio={} 
        free={} 

        for x in fechas:
            filter_condition = (df['release_date'] == x) & (df['developer'] == developer) 
            developer_releases = df[filter_condition]
            if len(developer_releases) != 0:
                anio[x] = len(developer_releases)
                free[x] = len(developer_releases[developer_releases['price'] == 0.0])
        
        for y, i in free.items():
            free[y]=f'{round((i/anio[y])*100,2)}%'
        
        resultado = pd.DataFrame({'Año': anio.keys(),'Cantidad_items': anio.values(),'Contenido_Free': free.values()})
    return resultado.sort_values(by='Año',ascending=False)

#Funcion 2
df_2=dataset[['user_id','title','price','items_count','recommend']]
df_2=df_2.drop_duplicates(subset=['user_id','title'], keep='first').copy()

def user_info(user: str):
    try:
        if user not in df_2['user_id'].unique():
            return {f'El usuario {user}, no existe.'}
        else:
            df=df_2[df_2['user_id']==user]
            resultado = {
                'Usuario': user,
                'Dinero gastado': df['price'].sum(),
                'cantidad de items': df['items_count'].head(1).to_list()[0],
                'Porcentaje de recomendaciones': f'{float(round((df['recommend'].sum()/df["items_count"].head(1).to_list()[0])*100,2))}%'
            }

        return resultado
    except:
        return {'El usuario no se encuentra en la base de datos.'}
    
#Funcion 3
df_3=dataset[['developer','release_date','title','user_id','recommend','sentiment_analysis']]
df_3=df_3.drop_duplicates(subset=['developer','title','user_id'], keep='first').copy()
df_3['release_date']=df_3['release_date'].astype(int).copy()

def developer_of_year(year: int):
    if year in df_3['release_date'].unique():
        anio=df_3[df_3['release_date']==year].sort_values(by='release_date', ascending=False)
        anio['rating']=anio['recommend']+anio['sentiment_analysis']
        respuesta=anio.groupby(by='developer')['rating'].sum().reset_index()
        respuesta.columns=['Desarrollador','Cantidad']
        respuesta=respuesta.sort_values(by='Cantidad', ascending=False).head(3).reset_index(drop=True)
        respuesta.index+=1
        return respuesta
    else:
        respuesta = f'Error: inserte un año que se encuentre en el rango {df_3['release_date'].min()} - {df_3['release_date'].max()}'
    return respuesta

#Funcion 4
df_4=dataset[['developer','user_id','sentiment_analysis']]
df_4=df_4.drop_duplicates(subset=['developer','user_id'],keep='first').copy()

def review_developer(dev: str):
    try:
        df=df_4[df_4['developer']==dev]
        positivo=df[df['sentiment_analysis']==2].shape[0]
        negativo=df[df['sentiment_analysis']==0].shape[0]
        respuesta = pd.DataFrame([{'Desarrollador':dev,'Positivo':positivo,'Negativo':negativo}])
        return respuesta
    except:
        return {'No ingreso un valor relevante, o el desarrollador no tiene Resenias'}

#Funcion 5
df_5=pd.read_parquet(r'C:\Users\Moises\Desktop\Projecto invidual 1\archivos limpios\criterio3.parquet')

def user_for_genre(gen: str):
    try:
        df=df_5[df_5['genres']==gen]
        usuario= df.groupby('user_id')['playtime_forever'].sum().idxmax(0)
        df_full=df[df['user_id']==usuario]
        horas=df_full.groupby('release_date')['playtime_forever'].sum().reset_index()
        horas.sort_values(by='release_date',ascending=False,inplace=True)
        horas.columns=['Año','Tiempo']
        horas_str = horas.to_string(index=False)
        return {f'El usuario con mayor tiempo acumulado jugando juegos del genero {gen} es: {usuario}\n {horas_str}'}
    except:
        return 'Error: el valor ingresado no se encuentra en el dataset o valor incorrecto'
