# tp_JSON-LD

get_issues.py arguments: 

  -Un argument obligatoire donnant le nom du dépôt, sous la forme owner/repo.
  
  -Un argument optionnel --out indique dans quel fichier écrire les données récupérées. (si le fichier existe déjà, son contenu sera remplacé. Si cet argument n’es pas spécifié, les données seront écrites sur la sortie standard)
  
  
  -Un argument optionnel --prev permet de spécifier le chemin d’un fichier précédemment produit par le script, pour le même dépôt. Le script interrogera alors l’API de github de telle manière à ne récupérer que les éléments plus récents que ceux ayant déjà été récupérés.
  
  -Un argument optionnel --auth permet de spécifier un jeton d’authentification github, qui peut être créé sur https://github.com/settings/tokens.
