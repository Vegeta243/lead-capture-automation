# 📦 INFORMATIONS IMPORTANTES - Lead Capture Automation

**Date de création** : 21 janvier 2026

## ✅ État du projet

Le système d'automatisation de capture de leads est **configuré à 90%**. Consultez [ETAPES_RESTANTES.md](ETAPES_RESTANTES.md) pour terminer la configuration.

**Secrets GitHub restants à configurer** (2 actions manuelles requises):
- `GOOGLE_SERVICE_ACCOUNT_JSON`: Contenu du fichier JSON téléchargé
- `SMTP_PASSWORD`: Mot de passe d'application Gmail (16 caractères)

### Ce qui a été fait :

✔️ **Dépôt GitHub** : Créé avec tous les fichiers nécessaires
✔️ **Workflows GitHub Actions** : 3 workflows configurés et opérationnels
✔️ **Scripts Python** : Tous les scripts de traitement créés
✔️ **Projet Google Cloud** : `lead-capture-automation-485018`
✔️ **API Google Sheets** : Activée
✔️ **Compte de service Google** : `lead-capture-bot`
✔️ **Clé JSON du compte de service** : Téléchargée (fichier : `lead-capture-automation-485018-48d971ea5238.json`)
✔️ **Google Sheet** : Créée avec structure complète
✔️ **Documentation** : README.md et SETUP.md complets

---

## 🔑 Informations sensibles

### Compte de service Google Cloud

- **Nom du projet** : `lead-capture-automation-485018`
- **Nom du compte de service** : `lead-capture-bot`
- **Email du compte de service** : `lead-capture-bot@lead-capture-automation-485018.iam.gserviceaccount.com`
- **Fichier de clé JSON** : `lead-capture-automation-485018-48d971ea5238.json` (❗ Téléchargé dans votre dossier Téléchargements)

### Google Sheet

- **Nom** : "Leads - Lead Capture Automation"
- **ID de la feuille** : `1GCQY1pNmuqqf-rnW5OvW-lEPegntl25Hg9kbWm-yChM`
- **URL** : https://docs.google.com/spreadsheets/d/1GCQY1pNmuqqf-rnW5OvW-lEPegntl25Hg9kbWm-yChM/edit

**⚠️ ACTION REQUISE** : Vous devez partager cette feuille avec le compte de service en ajoutant l'email ci-dessus avec les droits "Éditeur".

---

## 🛠️ Configuration des secrets GitHub

Vous devez maintenant configurer les 7 secrets GitHub Actions dans **Settings > Secrets and variables > Actions** :

### Secrets à configurer :

1. **GOOGLE_SERVICE_ACCOUNT_JSON**
   - Ouvrez le fichier `lead-capture-automation-485018-48d971ea5238.json` téléchargé
   - Copiez TOUT le contenu du fichier JSON
   - Collez-le dans ce secret

2. **GOOGLE_SHEET_ID**
   - Valeur : `1GCQY1pNmuqqf-rnW5OvW-lEPegntl25Hg9kbWm-yChM`

3. **SLACK_WEBHOOK_URL** (Optionnel)
   - Si vous souhaitez des notifications Slack, créez un webhook sur https://api.slack.com/apps
   - Sinon, vous pouvez ignorer ce secret (le système fonctionnera sans)

4. **SMTP_SERVER**
   - Pour Gmail : `smtp.gmail.com`
   - Pour Outlook : `smtp-mail.outlook.com`

5. **SMTP_PORT**
   - Généralement : `587`

6. **SMTP_EMAIL**
   - Votre adresse email pour envoyer les emails automatiques

7. **SMTP_PASSWORD**
   - **Pour Gmail** : Vous devez créer un "Mot de passe d'application"
     1. Allez sur https://myaccount.google.com/security
     2. Activez la validation en 2 étapes si ce n'est pas déjà fait
     3. Cliquez sur "Mots de passe des applications"
     4. Créez une nouvelle application personnalisée
     5. Copiez le mot de passe généré (16 caractères)

---

## 🚀 Prochaines étapes

### Étape 1 : Partager la Google Sheet
1. Ouvrez https://docs.google.com/spreadsheets/d/1GCQY1pNmuqqf-rnW5OvW-lEPegntl25Hg9kbWm-yChM/edit
2. Cliquez sur "Partager" en haut à droite
3. Ajoutez : `lead-capture-bot@lead-capture-automation-485018.iam.gserviceaccount.com`
4. Sélectionnez le rôle "Éditeur"
5. Décochez "Avertir les utilisateurs" (optionnel)
6. Cliquez sur "Envoyer"

### Étape 2 : Configurer les secrets GitHub
1. Allez sur https://github.com/Vegeta243/lead-capture-automation/settings/secrets/actions
2. Configurez les 7 secrets listés ci-dessus
3. Utilisez le guide SETUP.md pour plus de détails

### Étape 3 : Tester le système
1. Allez dans l'onglet "Actions" : https://github.com/Vegeta243/lead-capture-automation/actions
2. Sélectionnez "Lead Webhook Trigger"
3. Cliquez sur "Run workflow"
4. Remplissez les informations de test :
   - Nom complet : Test Lead
   - Email : test@example.com
   - Téléphone : +33 6 12 34 56 78
5. Vérifiez que le lead apparaît dans votre Google Sheet

---

## 📚 Documentation

- **README.md** : Vue d'ensemble du projet et guide d'utilisation
- **SETUP.md** : Guide détaillé de configuration avec instructions pas-à-pas
- **requirements.txt** : Dépendances Python nécessaires

---

## 📅 Workflows automatiques

Une fois configuré, le système exécutera automatiquement :

1. **Lead Webhook Trigger** (Manuel)
   - Traite un nouveau lead
   - Enregistre dans Google Sheets
   - Envoie notification Slack

2. **Send Scheduled Emails** (Quotidien à 9h00 UTC)
   - Vérifie les leads nécessitant un suivi
   - Envoie des emails de suivi automatiques après 48h

3. **Daily Lead Report** (Quotidien à 18h00 UTC)
   - Génère un rapport des leads du jour
   - Envoie le rapport via Slack

---

## ⚠️ Important : Sécurité

- ❌ **NE JAMAIS** committer le fichier JSON du compte de service dans Git
- ❌ **NE JAMAIS** partager les secrets GitHub Actions
- ✅ Le fichier JSON doit rester dans votre dossier Téléchargements
- ✅ Les secrets sont cryptés par GitHub et inaccessibles aux autres

---

## 👫 Support

Pour toute question :
1. Consultez d'abord SETUP.md
2. Vérifiez les logs des workflows dans l'onglet "Actions"
3. Ouvrez une issue sur GitHub si nécessaire

---

**Créé avec ❤️ pour automatiser votre capture de leads**
