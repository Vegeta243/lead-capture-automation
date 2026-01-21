# Guide de configuration - Lead Capture Automation

Ce guide vous aidera à configurer tous les secrets nécessaires pour faire fonctionner le système d'automatisation de capture de leads.

## 📋 Secrets requis

Le système nécessite 7 secrets GitHub Actions pour fonctionner correctement :

### 1. GOOGLE_SERVICE_ACCOUNT_JSON
**Requis** : Oui
**Description** : Clé de compte de service Google Cloud pour accéder à Google Sheets API

**Comment l'obtenir** :
1. Accédez à [Google Cloud Console](https://console.cloud.google.com/)
2. Créez un nouveau projet ou sélectionnez un projet existant
3. Activez l'API Google Sheets
   - Allez dans "APIs & Services" > "Enable APIs and Services"
   - Recherchez "Google Sheets API" et activez-la
4. Créez un compte de service
   - Allez dans "IAM & Admin" > "Service Accounts"
   - Cliquez sur "Create Service Account"
   - Donnez-lui un nom (ex: "lead-capture-bot")
   - Cliquez sur "Create and Continue"
5. Créez une clé JSON
   - Cliquez sur le compte de service créé
   - Allez dans l'onglet "Keys"
   - Cliquez sur "Add Key" > "Create new key"
   - Sélectionnez le format JSON
   - La clé sera téléchargée automatiquement
6. Copiez tout le contenu du fichier JSON téléchargé

**Format attendu** : JSON complet du fichier de clés
```json
{
  "type": "service_account",
  "project_id": "your-project",
  "private_key_id": "...",
  "private_key": "...",
  ...
}
```

---

### 2. GOOGLE_SHEET_ID
**Requis** : Oui
**Description** : ID de votre Google Sheet où les leads seront stockés

**Comment l'obtenir** :
1. Créez une nouvelle Google Sheet ou ouvrez une existante
2. L'URL ressemble à : `https://docs.google.com/spreadsheets/d/VOTRE_SHEET_ID/edit`
3. Copiez la partie `VOTRE_SHEET_ID` de l'URL
4. **IMPORTANT** : Partagez la feuille avec l'email du compte de service
   - Ouvrez votre Google Sheet
   - Cliquez sur "Partager"
   - Ajoutez l'email du compte de service (trouvé dans le JSON, champ `client_email`)
   - Donnez-lui les droits "Éditeur"

**Format attendu** : Chaîne de caractères (ID uniquement)
```
1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
```

---

### 3. SLACK_WEBHOOK_URL
**Requis** : Non (optionnel)
**Description** : Webhook Slack pour recevoir des notifications sur les nouveaux leads et rapports quotidiens

**Comment l'obtenir** :
1. Accédez à [Slack API](https://api.slack.com/apps)
2. Créez une nouvelle application Slack ou sélectionnez une existante
3. Activez "Incoming Webhooks"
4. Créez un nouveau webhook pour un canal spécifique
5. Copiez l'URL du webhook

**Format attendu** : URL complète du webhook
```
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX
```

**Note** : Si vous ne configurez pas ce secret, le système fonctionnera mais sans notifications Slack.

---

### 4. SMTP_SERVER
**Requis** : Oui
**Description** : Serveur SMTP pour envoyer des emails de suivi automatiques

**Exemples de valeurs** :
- Gmail : `smtp.gmail.com`
- Outlook/Hotmail : `smtp-mail.outlook.com`
- Yahoo : `smtp.mail.yahoo.com`
- Office 365 : `smtp.office365.com`

**Format attendu** : Nom d'hôte du serveur SMTP
```
smtp.gmail.com
```

---

### 5. SMTP_PORT
**Requis** : Oui
**Description** : Port du serveur SMTP (généralement 587 pour TLS ou 465 pour SSL)

**Valeurs courantes** :
- Port 587 : STARTTLS (recommandé)
- Port 465 : SSL/TLS
- Port 25 : Non crypté (déconseillé)

**Format attendu** : Numéro de port
```
587
```

---

### 6. SMTP_EMAIL
**Requis** : Oui
**Description** : Adresse email utilisée pour envoyer les emails automatiques

**Format attendu** : Adresse email complète
```
votre.email@gmail.com
```

**Note pour Gmail** : Vous devrez activer "Mots de passe d'application" dans les paramètres de sécurité Google.

---

### 7. SMTP_PASSWORD
**Requis** : Oui
**Description** : Mot de passe de l'adresse email (ou mot de passe d'application)

**Pour Gmail** :
1. Activez la validation en 2 étapes sur votre compte Google
2. Allez dans [Paramètres de sécurité Google](https://myaccount.google.com/security)
3. Cliquez sur "Mots de passe des applications"
4. Sélectionnez "Application personnalisée" et donnez-lui un nom
5. Copiez le mot de passe généré (16 caractères sans espaces)

**Format attendu** : Mot de passe ou mot de passe d'application
```
abcdefghijklmnop
```

---

## 🔧 Configuration des secrets GitHub

1. Allez dans votre dépôt GitHub
2. Cliquez sur "Settings" (⚙️)
3. Dans le menu latéral, cliquez sur "Secrets and variables" > "Actions"
4. Cliquez sur "New repository secret"
5. Entrez le nom du secret (ex: `GOOGLE_SERVICE_ACCOUNT_JSON`)
6. Collez la valeur correspondante
7. Cliquez sur "Add secret"
8. Répétez pour chaque secret

## ✅ Vérification de la configuration

Une fois tous les secrets configurés :

1. Allez dans l'onglet "Actions" de votre dépôt
2. Sélectionnez le workflow "Lead Webhook Trigger"
3. Cliquez sur "Run workflow" pour tester manuellement
4. Vérifiez que le workflow s'exécute sans erreur

## 🚀 Utilisation

Après configuration, le système fonctionnera automatiquement :

- **Lead Webhook Trigger** : Déclenché manuellement via workflow_dispatch pour traiter un nouveau lead
- **Send Scheduled Emails** : S'exécute tous les jours à 9h00 UTC pour envoyer des emails de suivi
- **Daily Lead Report** : S'exécute tous les jours à 18h00 UTC pour générer un rapport quotidien

## ⚠️ Dépannage

### Erreur d'authentification Google Sheets
- Vérifiez que l'API Google Sheets est activée
- Vérifiez que le compte de service a accès à la feuille (partagée avec l'email du compte de service)
- Vérifiez que le JSON du compte de service est valide et complet

### Erreur d'envoi d'email
- Vérifiez les paramètres SMTP (serveur, port)
- Pour Gmail, vérifiez que vous utilisez un mot de passe d'application (pas votre mot de passe principal)
- Vérifiez que la validation en 2 étapes est activée sur votre compte

### Workflow échoue
- Consultez les logs du workflow dans l'onglet "Actions"
- Vérifiez que tous les secrets sont bien configurés
- Vérifiez qu'il n'y a pas d'espaces ou de caractères invisibles dans les valeurs des secrets

## 📚 Ressources supplémentaires

- [Documentation Google Cloud Service Accounts](https://cloud.google.com/iam/docs/service-accounts)
- [Documentation Google Sheets API](https://developers.google.com/sheets/api)
- [Documentation Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [Mots de passe d'application Gmail](https://support.google.com/accounts/answer/185833)
