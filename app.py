import streamlit as st


#レシピデータ
recettes = {
  "Mousse au Chocolat": {
    "Ingrédients":[
      "6     jaunes d'oeufs(J-OE)",
      "85g   de sucre",
      "310g  de chocolat noir(70%)",
      "500ml de créme montée"
    ],

    "Préparation":[
      "Faire ramollir le chocolat dans une casserole au bain-marie.",
      "Mélanger les J-OEs avec le sucre jusau'à l'obtention d'un mélange homogène et mousseux.",
      "Mélanger le chocolat fuondu et un peu de créme.",
      " Mélanger les J-OEs et la créme puis verser le 3 et mixer délicatement."
    ],
     "image":"images/mousse.JPG"
  },

    "Madeleine": {
    "Ingrédients":[
      "75g   de sucre",
      "75g   de la farine",
      "2.5g  de levure",
      "90g   des oeufs",
      "90g   de beurre",
      "2 cuil. vanille",
      "1/2 zeste de citron"
          ],
    "Préparation":[
      "Faire fondre le beurre.",
      "Mélanger les oeufs et le sucre, puis la farine et la levure.",
      "Mélanger le beurre, la vanille, et des zestes de citron.",
      "Laisser reposer au froid pendant 2 heures.",
      "Dans un moule de Madeleine verser la preparation jusqu'à 8/10 de moule.",
      "Enfourner à 200℃ pendant 12-15 min. "
    ],
         "image":"images/madeleine.JPG"

       },
    "Cake au Chocolat": {
    "Ingrédients":[
      "125g  de beurre",
      "125g  de sucre",
      "2     oeufs",
      "1     zeste de citron et d'orange",
      "125g  de la farine",
      "2.5g  de levure",
      "≪base de chocolat≫",
      "12g   de poudre de cacao",
      "5g    de beurre fondu",
      "25g   de lait",
          ],
    "Préparation":[
      "Faire ramollir du beurre et mélanger avec du sucre et les zestes.",
      "Mettre les oeufs petit à petit.",
      "Mélanger la farine et la levure.",
      "Dans un autre bol,mettez tous les ingrédients de ≪base de chocolat≫ et mélangez bien.",
      "Mélanger la ≪base de chocolat≫ et 1/3 d'appareil.",
      "Pocher l'appareil blanc et l'appareil chocolat alternativement.",
      "Enfourner à 170℃ pendant 40-45 min. "
    ],
         "image":"images/cake au chocolat.jpg"

       },
      "Crème brûlée": {
    "Ingrédients":[
      "200g du lait",
      "200g de la crème",
      "2    gousse de vanille",
      "70g de sucre",
      "4    jaunes d'oeufs(J-OE)",
      "3g  de la gélatine"
          ],
    "Préparation":[
      "Faire fondre la gélatine avec d'eau et des glaçons.",
      "Dans une casserole, mettez du lait, de la crème, de gousse de vanille,et 1/3 du sucre,puis chauffer jusqu'à un peu avant que ça bout.",
      "Dans un saladier, mettez le reste de sucre et du J-OE et mélangez bien au fouet.",
      "Verser la casserole dans le saladier petit à petit, et ajouter la gélatine.",
      "Chinoiser les ingrédients pour enlever des bulle d'air.",
      "Dans les cocottes,versez un par un, puis enfourner à 120-130℃ pendant 20-30 min.",
      "Après la cuisson, une fois la crème bien refroidie avant de la persemer de sucre roux en surface, puis répartir le sucre en une fine couche.",
      "Caraméliser la surface de la crème avec un chalumeau, et déguster juste après."
    ],
         "image":"images/crème brûlée.jpg"

       },
    "Biscuit Chocolat": {
    "Ingrédients":[
      "4     oeufs",
      "130g   de sucre",
      "90g   de farine",
      "20g   de poudre d'amandes",
      "26g   de cacao en poudre",
      "15g   de beurre"
    ],

    "Préparation":[
      "Faire fondre le beurre.",
      "Mélanger le sucre et les oeufs dans un cul de poule, puis fouetter au fouet sur un bain-marie 65℃ pendant quelques minutes, et terminer de battre au batteur jusqu'à complet refroidisse,ent",
      "Tamiser la farine, le poudre d'amande et le cacao sur la préparation, à l'aide d'une passoire fine en remuant délicatement avec une maryse",
      "Verser le beurre fondu dedans et mélanger délicatement ",
      "Verser la préparation dans le moule, et enfourner à four à 180℃ pendant 20-25 min."
    ],
      "image":"images/biscuit et forêt noir.png"
  },   
"Chouquettes": {
    "Ingrédients":[
      "200g d'eau",
      "80g de beurre",
      "2g  de sel",
      "2g  de sucre",
      "120g de farine",
      "4   oeufs",
      "sucre casson"
    ],

    "Préparation":[
      "Mettre l'eau, le beurre, le sucre et le sel dans une casserole sur le feu. Porter à ébullition.",
      "Retirer du feu et verser la farine en une seule fois. Mélanger à la spatule en bois en prenant soin de ne pas laisser de grumeau.",
      "Dessécher la pâte sur le feu en remuant avec la spatule en bois, jusqu'à ce qu'elle se détache des parois de la casserole et qu'elle forme une boule.",
      "Laisser refroidire 5min, puis incorporer les oeufs un à un.",
      "Sur une plaque, dresser les choux en pressant doucement sur la poche à douille. Avec un pinceau, dorer la surface des choux au jaune d'oeuf.",
      "Couvrir la surface des choux de sucre en grains et cuire à four à 180℃ pendant 20-30 min."
    ],
      "image":"images/chouquettes.jpg"
  },   

}


#タイトル
st.sidebar.markdown("<h3 style='color:purple;'>Recette de Gateaux</h3>",unsafe_allow_html=True)

#サイドバーでレシピを選択
recette_name = st.sidebar.selectbox("choisissez la recette",
list(recettes.keys()))

#選択したレシピを表示
if recette_name:
  #レシピの名前の色を変更
    st.markdown(f"<h2 style='color:purple;'>{recette_name}</h2>", unsafe_allow_html=True)
    
    image_path =recettes[recette_name]["image"]
    st.image(image_path,caption=recette_name)

   
  #材料
    st.subheader("Ingrédients")
    for ingredient in recettes[recette_name]["Ingrédients"]: 
      st.markdown(f"<p style='color:blue;'>- {ingredient}</p>",unsafe_allow_html=True)
  #作り方
    st.subheader("Préparation")
    for idx, Préparation in enumerate(recettes[recette_name]["Préparation"], 1): 
      st.markdown(f"<p style='color:blue;'>{idx}.{Préparation}</p>",unsafe_allow_html=True)
