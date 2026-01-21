# 🔧 Étapes Restantes pour Finaliser le Système

## ✅ Configuration Déjà Terminée

1. ✅ Projet Google Cloud créé: `lead-capture-automation-485018`
2. ✅ API Google Sheets activée
3. ✅ Compte de service créé: `lead-capture-bot@lead-capture-automation-485018.iam.gserviceaccount.com`
4. ✅ Clé JSON téléchargée: `lead-capture-automation-485018-67f92eb5e3fa.json` (dans votre dossier Téléchargements)
5. ✅ Feuille Google Sheets créée et partagée avec le compte de service
   - ID: `1GCQY1pNmuqqf-rnW5OvW-lEPegntl25Hg9kbWm-yChM`
   - Lien: https://docs.google.com/spreadsheets/d/1GCQY1pNmuqqf-rnW5OvW-lEPegntl25Hg9kbWm-yChM/edit
6. ✅ Secrets GitHub configurés:
   - `GOOGLE_SHEET_ID`
   - `SMTP_EMAIL` (elliottshilenge5@gmail.com)
   - `SMTP_SERVER` (smtp.gmail.com)
   - `SMTP_PORT` (587)

---

## 🚨 ACTIONS MANUELLES REQUISES

### 1. Ajouter le Secret GOOGLE_SERVICE_ACCOUNT_JSON

**Ce secret est CRITIQUE pour que le système fonctionne.**

#### Étapes:

1. Ouvrez votre dossier **Téléchargements**
2. Localisez le fichier: `lead-capture-automation-485018-67f92eb5e3fa.json`
3. Ouvrez ce fichier avec un éditeur de texte (Bloc-notes, Notepad++, etc.)
4. **Copiez TOUT le contenu** du fichier (Ctrl+A puis Ctrl+C)
5. Allez sur: https://github.com/Vegeta243/lead-capture-automation/settings/secrets/actions
6. Cliquez sur **"New repository secret"**
7. Nom du secret: `GOOGLE_SERVICE_ACCOUNT_JSON`
8. Valeur: **Collez tout le contenu JSON copié**
9. Cliquez sur **"Add secret"**

⚠️ **IMPORTANT**: Le contenu doit commencer par `{` et se terminer par `}`, et contenir toutes les informations du compte de service.

---

### 2. Créer un Mot de Passe d'Application Gmail

**Nécessaire pour envoyer des emails automatisés.**

#### Étapes:

1. Allez sur: https://myaccount.google.com/apppasswords
2. **Connectez-vous** avec votre compte Gmail: `elliottshilenge5@gmail.com`
3. **Complétez la vérification d'identité** demandée par Google
4. Une fois connecté:
   - Dans "Nom de l'application", entrez: `Lead Capture Automation`
   - Cliquez sur **"Créer"**
5. Google affichera un **mot de passe de 16 caractères** (format: xxxx xxxx xxxx xxxx)
6. **Copiez ce mot de passe** (vous ne pourrez plus le voir après)
7. Allez sur: https://github.com/Vegeta243/lead-capture-automation/settings/secrets/actions
8. Cliquez sur **"New repository secret"**
9. Nom du secret: `SMTP_PASSWORD`
10. Valeur: **Collez le mot de passe de 16 caractères** (gardez ou enlevez les espaces, les deux fonctionnent)
11. Cliquez sur **"Add secret"**

---

### 3. (Optionnel) Configurer Slack

Si vous voulez recevoir les notifications sur Slack:

1. Créez un webhook Slack sur: https://api.slack.com/messaging/webhooks
2. Ajoutez-le comme secret GitHub:
   - Nom: `SLACK_WEBHOOK_URL`
   - Valeur: L'URL du webhook

⚠️ Si vous ne configurez pas Slack, **le système fonctionnera quand même** (les notifications Slack seront simplement ignorées).

---

## 🧪 Test du Système

Une fois TOUS les secrets configurés:

### Test Manuel du Workflow

1. Allez sur: https://github.com/Vegeta243/lead-capture-automation/actions
2. Sélectionnez le workflow **"Lead Webhook Trigger"**
3. Cliquez sur **"Run workflow"** → **"Run workflow"**
4. Attendez que le workflow se termine
5. Vérifiez:
   - ✅ Le workflow est marqué comme réussi (coche verte)
   - ✅ Les données apparaissent dans la feuille Google Sheets
   - ✅ Un email de test a été reçu

### Test avec un Vrai Lead

Ajoutez un lead de test via votre formulaire et vérifiez que:
- Le lead est enregistré dans Google Sheets
- Vous recevez une notification (email et/ou Slack)

---

## 📊 Récapitulatif des Secrets Nécessaires

| Secret | Statut | Valeur |
|--------|--------|--------|
| `GOOGLE_SHEET_ID` | ✅ Configuré | `1GCQY1pNmuqqf-rnW5OvW-lEPegntl25Hg9kbWm-yChM` |
| `SMTP_EMAIL` | ✅ Configuré | `elliottshilenge5@gmail.com` |
| `SMTP_SERVER` | ✅ Configuré | `smtp.gmail.com` |
| `SMTP_PORT` | ✅ Configuré | `587` |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | ❌ À FAIRE | Contenu du fichier JSON téléchargé |
| `SMTP_PASSWORD` | ❌ À FAIRE | Mot de passe d'application Gmail 16 caractères |
| `SLACK_WEBHOOK_URL` | ⚪ Optionnel | URL du webhook Slack (si souhaité) |

---

## 📝 Fichiers de Référence

- **INFORMATIONS_IMPORTANTES.md**: Contient tous les détails du projet
- **SETUP.md**: Guide d'installation complet
- **README.md**: Documentation générale du projet

---

## 🆘 En Cas de Problème

Si le workflow échoue:

1. Vérifiez les logs dans l'onglet Actions
2. Assurez-vous que tous les secrets sont correctement configurés
3. Vérifiez que le compte de service a bien accès à la feuille Google Sheets
4. Testez la connexion Gmail avec le mot de passe d'application

---

**Bon courage ! Le système sera opérationnel à 100% une fois ces 2 secrets ajoutés.**
