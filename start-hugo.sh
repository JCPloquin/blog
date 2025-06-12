#!/bin/bash
echo "🎼 Lancement du site de Jean-Christophe Ploquin..."
hugo server -D --bind "127.0.0.1" &
sleep 3
xdg-open http://localhost:1313
echo "✅ Site ouvert dans le navigateur"
wait
