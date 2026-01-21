# 📧 Options SMTP pour Lead Capture Automation

## 🚨 Problème Actuel

Le mot de passe Gmail (`SMTP_PASSWORD`) ne peut pas être configuré car **Google exige l'activation de la validation en 2 étapes** avant de pouvoir créer des mots de passe d'application.

## ✅ Solutions Disponibles

### Option 1 : Activer la Validation en 2 Étapes Gmail (Recommandé)

**Avantages** : Gratuit, directement avec Gmail, sécurisé

**Étapes** :
1. Allez sur : https://myaccount.google.com/security
2. Cliquez sur "Validation en 2 étapes"
3. Suivez les instructions pour l'activer (SMS ou application Google Authenticator)
4. Une fois activée, allez sur : https://myaccount.google.com/apppasswords
5. Créez un mot de passe pour "Lead Capture Automation"
6. Ajoutez-le comme secret GitHub `SMTP_PASSWORD`

---

### Option 2 : Utiliser Brevo (Sendinblue) - Gratuit

**Avantages** : 300 emails/jour gratuits, pas besoin de validation 2FA

**Étapes** :
1. Créez un compte gratuit : https://www.brevo.com/fr/
2. Allez dans "SMTP & API" → "SMTP"
3. Récupérez vos identifiants SMTP
4. Mettez à jour les secrets GitHub :
   - `SMTP_SERVER` : `smtp-relay.brevo.com` (au lieu de smtp.gmail.com)
   - `SMTP_PORT` : `587` (garder)
   - `SMTP_EMAIL` : Votre email Brevo ou elliottshilenge5@gmail.com
   - `SMTP_PASSWORD` : La clé SMTP Brevo

---

### Option 3 : Utiliser SendGrid - Gratuit

**Avantages** : 100 emails/jour gratuits, intégration simple

**Étapes** :
1. Créez un compte gratuit : https://sendgrid.com/
2. Générez une clé API
3. Mettez à jour les secrets GitHub :
   - `SMTP_SERVER` : `smtp.sendgrid.net`
   - `SMTP_PORT` : `587`
   - `SMTP_EMAIL` : `apikey` (exactement comme ça)
   - `SMTP_PASSWORD` : Votre clé API SendGrid

---

### Option 4 : Utiliser Mailgun - Gratuit

**Avantages** : 5000 emails/mois gratuits pendant 3 mois

**Étapes** :
1. Créez un compte : https://www.mailgun.com/
2. Configurez un domaine (ou utilisez le sandbox)
3. Récupérez les identifiants SMTP
4. Mettez à jour les secrets GitHub :
   - `SMTP_SERVER` : `smtp.mailgun.org`
   - `SMTP_PORT` : `587`
   - `SMTP_EMAIL` : Votre login SMTP Mailgun
   - `SMTP_PASSWORD` : Votre mot de passe SMTP Mailgun

---

## 🛠️ Solution Temporaire : Tester sans Email

Le système peut fonctionner **partiellement** sans SMTP_PASSWORD :
- ✅ Les leads seront enregistrés dans Google Sheets
- ✅ Les workflows GitHub Actions fonctionneront
- ❌ Les notifications par email ne fonctionneront pas (erreur attendue)
- ✅ Les notifications Slack fonctionneront (si configuré)

**Pour tester** :
1. Allez sur : https://github.com/Vegeta243/lead-capture-automation/actions
2. Sélectionnez "Lead Webhook Trigger"
3. Cliquez sur "Run workflow"
4. Vérifiez que les données apparaissent dans Google Sheets

---

## 📊 Comparaison des Options

| Service | Emails Gratuits | Nécessite 2FA | Complexité | Recommandation |
|---------|----------------|---------------|-------------|----------------|
| **Gmail** | Illimité | Oui | Moyenne | ⭐⭐⭐⭐⭐ Meilleure si 2FA activée |
| **Brevo** | 300/jour | Non | Facile | ⭐⭐⭐⭐ Excellente alternative |
| **SendGrid** | 100/jour | Non | Facile | ⭐⭐⭐⭐ Très bonne option |
| **Mailgun** | 5000/mois | Non | Moyenne | ⭐⭐⭐ Bonne pour gros volume |

---

## ⚡ Ma Recommandation

### Choix 1 : Gmail avec 2FA (5 minutes)
Si vous pouvez activer la validation en 2 étapes, c'est la solution la plus simple.

### Choix 2 : Brevo (10 minutes)
Si vous ne voulez pas activer la 2FA Gmail, Brevo est la meilleure alternative gratuite.

---

## 📝 Statut Actuel du Système

**Avancé à 95%** :
- ✅ Google Cloud configuré
- ✅ Google Sheets prêt
- ✅ 5/6 secrets GitHub configurés
- ✅ Workflows GitHub Actions opérationnels
- ❌ 1 secret manquant : `SMTP_PASSWORD`

**Une fois le dernier secret ajouté, le système sera 100% fonctionnel.**
