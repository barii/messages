# Prod

## Download
```bash
gcloud storage cp --recursive gs://emojiwho-prod.appspot.com/static_data ./static_data
gcloud storage cp --recursive gs://emojiwho-prod.appspot.com/message_presets ./message_presets

## Upload
```bash
gcloud storage cp --recursive ./static_data gs://emojiwho-prod.appspot.com/
gcloud storage cp --recursive ./message_presets gs://emojiwho-prod.appspot.com/message_presets

# Staging

## Download
```bash
gcloud storage cp --recursive gs://emj-staging.appspot.com/static_data ./static_data
gcloud storage cp --recursive gs://emj-staging.appspot.com/message_presets ./message_presets

## Upload
```bash
gcloud storage cp --recursive ./static_data gs://emj-staging.appspot.com/
gcloud storage cp --recursive ./message_presets gs://emj-staging.appspot.com/message_presets

# Dev

## Download
```bash
gcloud storage cp --recursive gs://emojiwho-dev-784d0.appspot.com/static_data ./static_data
gcloud storage cp --recursive gs://emojiwho-dev-784d0.appspot.com/message_presets ./message_presets

## Upload
```bash
gcloud storage cp --recursive ./static_data gs://emojiwho-dev-784d0.appspot.com/
gcloud storage cp --recursive ./message_presets gs://emojiwho-dev-784d0.appspot.com/message_presets