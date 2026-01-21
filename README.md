# 🚀 Lead Capture Automation

Système automatique de capture et de gestion de leads avec GitHub Actions, Google Sheets, Slack et Gmail.

## 🎯 Objectif

Ce projet automatise complètement le processus de capture et de suivi des leads pour votre entreprise :

- **Capture automatique** : Les leads sont capturés via un formulaire web ou un webhook
- **Stockage centralisé** : Tous les leads sont enregistrés dans Google Sheets
- **Notifications instantanées** : Notifications Slack pour chaque nouveau lead
- **Suivi automatisé** : Emails de suivi automatiques envoyés selon un calendrier configurable
- **Rapports quotidiens** : Rapport récapitulatif journalier des nouveaux leads

## ✨ Fonctionnalités

### 📝 Capture de leads
- Traitement automatique des informations des leads
- Validation et formatage des données
- Enregistrement dans Google Sheets avec horodatage
- Notification Slack immédiate

### 📧 Emails automatiques
- Envoi d'emails de suivi programmés
- Templates personnalisables
- Gestion des délais configurable (48h après réception)
- Support de plusieurs scénarios de suivi

### 📊 Rapports quotidiens
- Génération automatique de rapports
- Envoi quotidien via Slack
- Statistiques sur les nouveaux leads
- Résumé des actions de la journée

## 🛠️ Technologies utilisées

- **GitHub Actions** : Automatisation des workflows
- **Python 3.11** : Langage de programmation principal
- **Google Sheets API** : Stockage et gestion des données
- **Slack Webhooks** : Notifications en temps réel
- **SMTP (Gmail)** : Envoi d'emails automatiques

## 📚 Configuration

Le système nécessite la configuration de 7 secrets GitHub Actions. Pour un guide complet de configuration, consultez :

**➡️ [SETUP.md](./SETUP.md) - Guide de configuration détaillé**

Le guide de configuration inclut :
- Instructions détaillées pour chaque secret requis
- Étapes pour créer un compte de service Google Cloud
- Configuration des webhooks Slack
- Configuration SMTP pour Gmail
- Dépannage des problèmes courants

### Secrets requis

1. `GOOGLE_SERVICE_ACCOUNT_JSON` - Compte de service Google Cloud
2. `GOOGLE_SHEET_ID` - ID de votre Google Sheet
3. `SLACK_WEBHOOK_URL` - Webhook Slack (optionnel)
4. `SMTP_SERVER` - Serveur SMTP (ex: smtp.gmail.com)
5. `SMTP_PORT` - Port SMTP (ex: 587)
6. `SMTP_EMAIL` - Adresse email d'envoi
7. `SMTP_PASSWORD` - Mot de passe d'application

## 🔄 Workflows GitHub Actions

### 1. Lead Webhook Trigger
**Déclenchement** : Manuel (workflow_dispatch)
**Fonction** : Traite un nouveau lead et l'enregistre dans le système

### 2. Send Scheduled Emails
**Déclenchement** : Quotidien à 9h00 UTC (cron)
**Fonction** : Envoie des emails de suivi aux leads selon le calendrier configuré

### 3. Daily Lead Report
**Déclenchement** : Quotidien à 18h00 UTC (cron)
**Fonction** : Génère et envoie un rapport quotidien des leads

## 📁 Structure du projet

```
lead-capture-automation/
├── .github/
│   └── workflows/
│       ├── lead-webhook-trigger.yml
│       ├── send-scheduled-emails.yml
│       └── daily-lead-report.yml
├── config/
│   └── leads_config.json
├── scripts/
│   ├── process_lead.py
│   ├── send_email.py
│   └── generate_report.py
├── requirements.txt
├── README.md
└── SETUP.md
```

## 🚀 Démarrage rapide

1. **Clonez ou forkez ce dépôt**

2. **Configurez les secrets GitHub Actions**
   - Suivez le guide dans [SETUP.md](./SETUP.md)
   - Configurez les 7 secrets requis

3. **Testez le système**
   - Allez dans l'onglet "Actions"
   - Sélectionnez "Lead Webhook Trigger"
   - Cliquez sur "Run workflow"
   - Remplissez les informations de test

4. **Vérifiez les résultats**
   - Consultez votre Google Sheet
   - Vérifiez les notifications Slack
   - Consultez les logs du workflow

## 📖 Utilisation

### Traiter un nouveau lead manuellement

1. Allez dans l'onglet **Actions**
2. Sélectionnez le workflow **Lead Webhook Trigger**
3. Cliquez sur **Run workflow**
4. Remplissez les informations du lead :
   - Nom complet
   - Email
   - Téléphone
   - Entreprise (optionnel)
   - Secteur d'activité (optionnel)
   - Besoins (optionnel)
5. Cliquez sur **Run workflow**

### Intégration avec un formulaire web

Vous pouvez déclencher le workflow via l'API GitHub Actions depuis votre formulaire web :

```bash
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/Vegeta243/lead-capture-automation/actions/workflows/lead-webhook-trigger.yml/dispatches \
  -d '{
    "ref":"main",
    "inputs":{
      "full_name":"Jean Dupont",
      "email":"jean.dupont@example.com",
      "phone":"+33612345678",
      "company":"ACME Corp",
      "business_sector":"Tech",
      "needs":"Site web e-commerce"
    }
  }'
```

## 🔧 Configuration avancée

### Personnaliser les délais d'envoi d'emails

Modifiez le fichier `config/leads_config.json` :

```json
{
  "email_delay_hours": 48,
  "daily_report_time": "18:00",
  "email_check_time": "09:00"
}
```

### Personnaliser les horaires des workflows

Modifiez les fichiers de workflow dans `.github/workflows/` :

```yaml
on:
  schedule:
    - cron: '0 9 * * *'  # Tous les jours à 9h00 UTC
```

## 🐛 Dépannage

### Les workflows échouent

1. Vérifiez que tous les secrets sont correctement configurés
2. Consultez les logs dans l'onglet "Actions"
3. Vérifiez que l'API Google Sheets est activée
4. Vérifiez que le compte de service a accès à votre Google Sheet

### Les emails ne sont pas envoyés

1. Vérifiez les paramètres SMTP
2. Pour Gmail, utilisez un mot de passe d'application (pas votre mot de passe principal)
3. Vérifiez que la validation en 2 étapes est activée

### Les notifications Slack ne fonctionnent pas

1. Vérifiez l'URL du webhook Slack
2. Assurez-vous que le webhook est activé dans votre workspace Slack

## 📝 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier pour vos propres besoins.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📞 Support

Pour toute question ou problème :

1. Consultez d'abord [SETUP.md](./SETUP.md)
2. Vérifiez les issues existantes
3. Ouvrez une nouvelle issue si nécessaire

---

**Fait avec ❤️ pour automatiser votre capture de leads**
