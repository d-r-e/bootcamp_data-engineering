export PGDATA=$HOME/.brew/var/postgres
source ~/.zshrc
pg_ctl start #server start
psql -d appstore_games #client start