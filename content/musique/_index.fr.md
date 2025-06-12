---
title: "Musique"
---

## Compositeur électroacoustique

Passionné par l’exploration sonore et la composition contemporaine, je développe un univers électroacoustique singulier, mêlant textures immersives et expérimentations interactives.

### Ascendance - Teaser exclusif {#ascendance-intro}

Prenez les commandes d'un vaisseau temporel pour explorer les généalogies. 
La musique s'adapte à chaque arbre généalogique dans ce jeu unique mêlant 
électroacoustique et généalogie.

<div style="max-width:640px; margin:2rem auto;" id="ascendance">
  {{< youtube BnqcQcPKJ-s >}}
</div>

🎮 **Bientôt disponible sur itch.io**  
🎵 **Musique adaptative et immersive**  
⏱️ **Gameplay innovant**

[Suivre le développement sur itch.io](https://jcploquin.itch.io)

### Aquastasis (extrait) - Premier mouvement d'"Hydrophonia" - Poème symphonique électroacoustique créé pour le Festival Nautil'Art 2023 à Rouen

Aquastasis explore l'équilibre aquatique primordial dans une approche inspirée de Reich et Glass.

🌊 Festival Nautil'Art 2023 - Halle aux Toiles (Rouen)

🎼 Composition cyclique sans début ni fin

🎯 Musique haptique et immersive

<div style="max-width:640px; margin:2rem auto;">
{{< soundcloud 2101981986 >}}
</div>

### Albums acousmatiques

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin: 2rem 0;">
  <div style="text-align:center; margin-bottom: 1rem;">
    {{< cd-img src="/img/opus1.jpg" alt="Opus 1" width="280px" id="opus1" >}}
    <div style="margin-top:0.5em;"><strong>Opus 1 : pièces acousmatiques de jeunesse</strong></div>
  </div>
  <div style="text-align:center; margin-bottom: 1rem;">
    {{< cd-img src="/img/hydrophonia.jpg" alt="Hydrophonia" width="280px" id="hydrophonia" >}}
    <div style="margin-top:0.5em;"><strong>Hydrophonia</strong></div>
  </div>
</div>

## Guitariste

La guitare, c’est mon autre voix : du fingerpicking blues à la musique celtique, j’explore les cordes comme on explore des mondes, toujours à la recherche de nouvelles couleurs et de liberté sonore.

<div style="display: flex; flex-direction: column; gap: 1.7rem; align-items: center;">
  <div style="max-width: 560px; width: 100%;">
    <div class="video-responsive">
      {{< youtube ccW_xrrqibs >}}
    </div>
    <div style="margin-top:0.5em; text-align:center;"><strong>enregistré en public au Havre</strong></div>
  </div>
  
  <div style="max-width: 560px; width: 100%;">
    <div class="video-responsive">
      {{< youtube "Q_mZwhnbbCE?start=1980" >}}
    </div>
    <div style="margin-top:0.5em; text-align:center;"><strong>Junior Crehan's Favourite</strong></div>
  </div>
</div>

### Albums de guitare

<div style="display: flex; justify-content: center; gap: 80px; flex-wrap: wrap; margin: 2rem 0;">
  <div style="text-align:center;">
    {{< cd-img src="/img/eclectique.jpg" alt="Éclectique" width="300px" id="eclectique" >}}
    <div style="margin-top:0.5em;"><strong>Éclectique</strong></div>
  </div>
  <div style="text-align:center;">
    {{< cd-img src="/img/renaissance.jpg" alt="ReNaissance" width="300px" id="renaissance" >}}
    <div style="margin-top:0.5em;"><strong>ReNaissance</strong></div>
  </div>
  <div style="text-align:center;">
    {{< cd-img src="/img/normainn_cd.png" alt="Normainn" width="300px" id="normainn" >}}
    <div style="margin-top:0.5em;"><strong>Normainn : From Everywhere To Elsewhere</strong></div>
  </div>
</div>

<!-- Popup CD -->
<div id="cd-popup" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.85); z-index:10000; align-items:center; justify-content:center;">
  <div style="position:relative; width:95vw; max-width:500px; max-height:90vh; background:#222; color:#fff; border-radius:10px; box-shadow:0 8px 32px #000a; padding:2em; display:flex; flex-direction:column; overflow-y:auto;">
    <button onclick="closeCdPopup()" style="position:absolute; top:10px; right:20px; background:rgba(255,255,255,0.8); border:none; border-radius:50%; width:36px; height:36px; font-size:1.5em; cursor:pointer; z-index:10;">×</button>
    <div id="cd-popup-content"></div>
  </div>
</div>

<!-- Popup panier -->
<div id="panier-popup" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.85); z-index:20000; align-items:center; justify-content:center;">
  <div style="position:relative; width:95vw; max-width:600px; max-height:90vh; background:#222; color:#fff; border-radius:10px; box-shadow:0 8px 32px #000a; padding:2em; display:flex; flex-direction:column; overflow-y:auto;">
    <button onclick="fermerPanier()" style="position:absolute; top:10px; right:20px; background:rgba(255,255,255,0.8); border:none; border-radius:50%; width:36px; height:36px; font-size:1.5em; cursor:pointer; z-index:10;">×</button>
    <div id="panier-content"></div>
    <div style="margin-top:1em; display:flex; gap:1em; justify-content:center;">
      <button onclick="fermerPanier()" style="padding:0.5em 1em; background:#777; color:#fff; border:none; border-radius:4px; cursor:pointer;">Continuer vos achats</button>
      <button onclick="validerPanier()" style="padding:0.5em 1em; background:#4CAF50; color:#fff; border:none; border-radius:4px; cursor:pointer;">Valider le panier</button>
    </div>
  </div>
</div>

<!-- Bouton panier (à mettre dans le header ou en haut de page) -->
<button id="panier-btn" onclick="afficherPanier()" style="position:fixed; top:20px; right:20px; background:#222; color:#fff; border:none; border-radius:50%; width:50px; height:50px; font-size:1.5em; cursor:pointer; z-index:1000;">🛒</button>

