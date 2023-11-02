from google_auth_oauthlib.flow import InstalledAppFlow


def obter_token_acesso():
    scopes = ['https://www.googleapis.com/auth/gmail.send']
    redirect_uri = 'http://localhost:5000/'  # Substitua pela sua URI de redirecionamento

    flow_obj  = InstalledAppFlow.from_client_secrets_file('credenciais.json', scopes=scopes, redirect_uri=redirect_uri)

    authorization_url, state = flow_obj.authorization_url(access_type='offline', include_granted_scopes='true')
    print('Por favor, visite o seguinte URL para conceder acesso ao seu aplicativo:')
    print(authorization_url)

    authorization_response = redirect_uri
    flow_obj.fetch_token(authorization_response=authorization_response)

    credentials = flow_obj.credentials  # Obtenha as credenciais autenticadas

    return credentials.token