# Prod
## Download

```bash
gcloud storage cp --recursive gs://emojiwho-prod.appspot.com/static_data ./static_data
```

## Upload

```bash
gcloud storage cp -m --recursive ./static_data gs://emojiwho-prod.appspot.com/
```

## Sync upload
```bash
gcloud storage rsync --recursive ./static_data gs://emojiwho-prod.appspot.com/static_data
```

# Staging

## Download

```bash
gcloud storage cp --recursive gs://emj-staging.appspot.com/static_data ./static_data
```

## Upload

```bash
gcloud storage cp -m --recursive ./static_data gs://emj-staging.appspot.com/
```

## Sync upload
```bash
gcloud storage rsync --recursive ./static_data gs://emj-staging.appspot.com/static_data
```

# Dev

## Download

```bash
gcloud storage cp --recursive gs://emojiwho-dev-784d0.appspot.com/static_data ./static_data
```

## Upload

```bash
gcloud storage cp -m --recursive ./static_data gs://emojiwho-dev-784d0.appspot.com/
```

## Sync upload
```bash
gcloud storage rsync --recursive ./static_data gs://emojiwho-dev-784d0.appspot.com/static_data

```
