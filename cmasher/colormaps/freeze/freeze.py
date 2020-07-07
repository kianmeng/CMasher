# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"


# %% GLOBALS AND DEFINITIONS
# Type of this colormap (according to viscm)
cm_type = "linear"

# RGB-values of this colormap
cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.50900473e-04, 2.21803191e-04, 2.89250261e-04],
           [8.75490123e-04, 7.64275127e-04, 1.03973501e-03],
           [1.82388438e-03, 1.57413245e-03, 2.22592534e-03],
           [3.07531017e-03, 2.62692935e-03, 3.84875237e-03],
           [4.61723855e-03, 3.90688107e-03, 5.91605079e-03],
           [6.44106962e-03, 5.40250460e-03, 8.43895457e-03],
           [8.54045410e-03, 7.10487745e-03, 1.14305979e-02],
           [1.09104712e-02, 9.00676571e-03, 1.49055235e-02],
           [1.35471685e-02, 1.11021260e-02, 1.88793762e-02],
           [1.64472795e-02, 1.33857952e-02, 2.33687315e-02],
           [1.96080395e-02, 1.58532839e-02, 2.83909946e-02],
           [2.30270587e-02, 1.85006330e-02, 3.39643410e-02],
           [2.67022312e-02, 2.13243096e-02, 4.01076809e-02],
           [3.06316681e-02, 2.43211292e-02, 4.64656995e-02],
           [3.48136459e-02, 2.74881967e-02, 5.28130137e-02],
           [3.92465665e-02, 3.08228593e-02, 5.91603356e-02],
           [4.37883705e-02, 3.43226701e-02, 6.55127258e-02],
           [4.82653005e-02, 3.79853422e-02, 7.18747124e-02],
           [5.26908305e-02, 4.17730329e-02, 7.82503148e-02],
           [5.70681892e-02, 4.55119491e-02, 8.46429426e-02],
           [6.14002137e-02, 4.92021733e-02, 9.10557904e-02],
           [6.56893983e-02, 5.28465878e-02, 9.74917667e-02],
           [6.99379447e-02, 5.64477730e-02, 1.03953538e-01],
           [7.41478021e-02, 6.00080497e-02, 1.10443565e-01],
           [7.83207208e-02, 6.35294560e-02, 1.16964432e-01],
           [8.24582278e-02, 6.70139169e-02, 1.23518150e-01],
           [8.65616826e-02, 7.04631867e-02, 1.30106595e-01],
           [9.06323033e-02, 7.38788453e-02, 1.36731655e-01],
           [9.46711739e-02, 7.72623403e-02, 1.43395115e-01],
           [9.86792853e-02, 8.06148938e-02, 1.50099220e-01],
           [1.02657468e-01, 8.39378049e-02, 1.56845208e-01],
           [1.06606472e-01, 8.72322259e-02, 1.63634525e-01],
           [1.10526959e-01, 9.04992060e-02, 1.70468649e-01],
           [1.14419539e-01, 9.37395581e-02, 1.77349824e-01],
           [1.18284683e-01, 9.69543187e-02, 1.84278764e-01],
           [1.22122817e-01, 1.00144350e-01, 1.91256717e-01],
           [1.25934319e-01, 1.03310316e-01, 1.98285612e-01],
           [1.29719475e-01, 1.06452980e-01, 2.05366589e-01],
           [1.33478507e-01, 1.09573134e-01, 2.12500391e-01],
           [1.37211606e-01, 1.12671257e-01, 2.19689093e-01],
           [1.40918878e-01, 1.15748048e-01, 2.26933472e-01],
           [1.44600381e-01, 1.18804175e-01, 2.34234247e-01],
           [1.48256134e-01, 1.21839906e-01, 2.41593984e-01],
           [1.51886080e-01, 1.24856082e-01, 2.49012238e-01],
           [1.55490125e-01, 1.27852961e-01, 2.56491323e-01],
           [1.59068119e-01, 1.30831175e-01, 2.64031582e-01],
           [1.62619859e-01, 1.33791103e-01, 2.71634502e-01],
           [1.66145092e-01, 1.36733226e-01, 2.79300983e-01],
           [1.69643507e-01, 1.39657962e-01, 2.87032146e-01],
           [1.73114749e-01, 1.42565777e-01, 2.94828820e-01],
           [1.76558393e-01, 1.45457001e-01, 3.02692451e-01],
           [1.79973988e-01, 1.48332253e-01, 3.10623017e-01],
           [1.83360964e-01, 1.51191614e-01, 3.18623123e-01],
           [1.86718780e-01, 1.54035869e-01, 3.26691891e-01],
           [1.90046752e-01, 1.56865225e-01, 3.34831289e-01],
           [1.93344163e-01, 1.59680122e-01, 3.43042141e-01],
           [1.96610263e-01, 1.62481181e-01, 3.51324414e-01],
           [1.99844170e-01, 1.65268726e-01, 3.59679571e-01],
           [2.03044930e-01, 1.68043147e-01, 3.68108801e-01],
           [2.06211583e-01, 1.70805144e-01, 3.76611835e-01],
           [2.09343035e-01, 1.73555235e-01, 3.85189390e-01],
           [2.12438107e-01, 1.76293967e-01, 3.93842128e-01],
           [2.15495473e-01, 1.79021790e-01, 4.02571320e-01],
           [2.18513791e-01, 1.81739455e-01, 4.11376888e-01],
           [2.21491598e-01, 1.84447696e-01, 4.20258991e-01],
           [2.24427300e-01, 1.87147256e-01, 4.29217935e-01],
           [2.27319181e-01, 1.89838941e-01, 4.38253912e-01],
           [2.30165399e-01, 1.92523632e-01, 4.47366983e-01],
           [2.32963971e-01, 1.95202292e-01, 4.56557058e-01],
           [2.35712772e-01, 1.97875975e-01, 4.65823880e-01],
           [2.38409517e-01, 2.00545841e-01, 4.75167004e-01],
           [2.41051650e-01, 2.03212984e-01, 4.84586659e-01],
           [2.43636541e-01, 2.05878837e-01, 4.94081806e-01],
           [2.46161412e-01, 2.08545021e-01, 5.03650889e-01],
           [2.48623231e-01, 2.11213233e-01, 5.13292456e-01],
           [2.51018451e-01, 2.13884951e-01, 5.23006709e-01],
           [2.53343678e-01, 2.16562403e-01, 5.32790656e-01],
           [2.55595132e-01, 2.19247827e-01, 5.42641884e-01],
           [2.57768395e-01, 2.21943295e-01, 5.52559570e-01],
           [2.59859325e-01, 2.24651788e-01, 5.62538980e-01],
           [2.61862891e-01, 2.27375947e-01, 5.72578004e-01],
           [2.63773897e-01, 2.30118934e-01, 5.82672767e-01],
           [2.65586961e-01, 2.32884393e-01, 5.92817827e-01],
           [2.67295992e-01, 2.35676035e-01, 6.03008475e-01],
           [2.68894266e-01, 2.38497832e-01, 6.13239860e-01],
           [2.70374966e-01, 2.41354445e-01, 6.23504590e-01],
           [2.71730644e-01, 2.44250844e-01, 6.33794883e-01],
           [2.72953265e-01, 2.47192402e-01, 6.44102113e-01],
           [2.74033905e-01, 2.50184796e-01, 6.54417502e-01],
           [2.74963524e-01, 2.53234439e-01, 6.64729396e-01],
           [2.75732509e-01, 2.56348199e-01, 6.75024834e-01],
           [2.76330200e-01, 2.59533241e-01, 6.85290629e-01],
           [2.76745438e-01, 2.62797272e-01, 6.95511594e-01],
           [2.76966851e-01, 2.66148538e-01, 7.05669970e-01],
           [2.76982578e-01, 2.69595641e-01, 7.15746310e-01],
           [2.76779406e-01, 2.73147310e-01, 7.25721140e-01],
           [2.76345187e-01, 2.76812743e-01, 7.35570337e-01],
           [2.75667131e-01, 2.80601046e-01, 7.45269095e-01],
           [2.74732651e-01, 2.84521185e-01, 7.54790720e-01],
           [2.73529659e-01, 2.88581732e-01, 7.64106860e-01],
           [2.72046335e-01, 2.92790603e-01, 7.73188499e-01],
           [2.70273406e-01, 2.97154712e-01, 7.82004172e-01],
           [2.68202347e-01, 3.01679622e-01, 7.90523350e-01],
           [2.65826682e-01, 3.06369242e-01, 7.98715952e-01],
           [2.63143039e-01, 3.11225423e-01, 8.06552739e-01],
           [2.60150856e-01, 3.16247729e-01, 8.14006900e-01],
           [2.56852104e-01, 3.21433367e-01, 8.21055176e-01],
           [2.53253104e-01, 3.26776866e-01, 8.27677752e-01],
           [2.49362984e-01, 3.32270371e-01, 8.33859898e-01],
           [2.45194039e-01, 3.37903775e-01, 8.39592115e-01],
           [2.40761420e-01, 3.43665045e-01, 8.44870373e-01],
           [2.36082814e-01, 3.49540616e-01, 8.49696069e-01],
           [2.31177748e-01, 3.55515916e-01, 8.54075760e-01],
           [2.26067103e-01, 3.61575849e-01, 8.58020621e-01],
           [2.20772647e-01, 3.67705261e-01, 8.61545739e-01],
           [2.15316912e-01, 3.73889281e-01, 8.64669372e-01],
           [2.09722622e-01, 3.80113712e-01, 8.67412181e-01],
           [2.04011687e-01, 3.86365464e-01, 8.69796342e-01],
           [1.98207159e-01, 3.92632245e-01, 8.71845144e-01],
           [1.92330524e-01, 3.98903275e-01, 8.73582010e-01],
           [1.86404358e-01, 4.05168723e-01, 8.75030465e-01],
           [1.80449691e-01, 4.11420319e-01, 8.76213169e-01],
           [1.74490034e-01, 4.17650452e-01, 8.77152578e-01],
           [1.68546894e-01, 4.23853140e-01, 8.77869515e-01],
           [1.62643518e-01, 4.30023172e-01, 8.78383946e-01],
           [1.56804241e-01, 4.36156229e-01, 8.78714672e-01],
           [1.51054670e-01, 4.42248820e-01, 8.78879260e-01],
           [1.45422007e-01, 4.48298184e-01, 8.78894035e-01],
           [1.39935365e-01, 4.54302202e-01, 8.78774107e-01],
           [1.34626051e-01, 4.60259311e-01, 8.78533411e-01],
           [1.29527801e-01, 4.66168426e-01, 8.78184765e-01],
           [1.24676907e-01, 4.72028869e-01, 8.77739936e-01],
           [1.20112195e-01, 4.77840306e-01, 8.77209706e-01],
           [1.15874927e-01, 4.83602670e-01, 8.76604003e-01],
           [1.12009050e-01, 4.89315996e-01, 8.75932293e-01],
           [1.08557405e-01, 4.94980857e-01, 8.75202383e-01],
           [1.05563996e-01, 5.00597768e-01, 8.74421939e-01],
           [1.03071660e-01, 5.06167284e-01, 8.73598257e-01],
           [1.01117658e-01, 5.11690391e-01, 8.72737080e-01],
           [9.97362361e-02, 5.17167760e-01, 8.71844810e-01],
           [9.89517149e-02, 5.22600528e-01, 8.70926074e-01],
           [9.87817190e-02, 5.27989508e-01, 8.69986256e-01],
           [9.92317239e-02, 5.33335890e-01, 8.69029150e-01],
           [1.00298678e-01, 5.38640571e-01, 8.68059272e-01],
           [1.01968013e-01, 5.43904721e-01, 8.67079827e-01],
           [1.04217186e-01, 5.49129362e-01, 8.66094260e-01],
           [1.07016305e-01, 5.54315526e-01, 8.65105670e-01],
           [1.10329834e-01, 5.59464315e-01, 8.64116556e-01],
           [1.14119375e-01, 5.64576717e-01, 8.63129574e-01],
           [1.18344837e-01, 5.69653748e-01, 8.62146959e-01],
           [1.22966144e-01, 5.74696417e-01, 8.61170639e-01],
           [1.27944650e-01, 5.79705671e-01, 8.60202537e-01],
           [1.33243818e-01, 5.84682423e-01, 8.59244411e-01],
           [1.38829708e-01, 5.89627595e-01, 8.58297667e-01],
           [1.44671431e-01, 5.94542047e-01, 8.57363710e-01],
           [1.50741167e-01, 5.99426598e-01, 8.56443848e-01],
           [1.57014085e-01, 6.04282046e-01, 8.55539184e-01],
           [1.63468241e-01, 6.09109149e-01, 8.54650734e-01],
           [1.70084366e-01, 6.13908621e-01, 8.53779450e-01],
           [1.76845638e-01, 6.18681141e-01, 8.52926169e-01],
           [1.83737442e-01, 6.23427349e-01, 8.52091660e-01],
           [1.90747139e-01, 6.28147840e-01, 8.51276644e-01],
           [1.97863840e-01, 6.32843171e-01, 8.50481780e-01],
           [2.05078239e-01, 6.37513871e-01, 8.49707559e-01],
           [2.12382351e-01, 6.42160405e-01, 8.48954621e-01],
           [2.19769403e-01, 6.46783207e-01, 8.48223497e-01],
           [2.27233705e-01, 6.51382677e-01, 8.47514595e-01],
           [2.34770479e-01, 6.55959169e-01, 8.46828353e-01],
           [2.42375695e-01, 6.60512982e-01, 8.46165327e-01],
           [2.50046100e-01, 6.65044389e-01, 8.45525889e-01],
           [2.57779086e-01, 6.69553624e-01, 8.44910364e-01],
           [2.65572433e-01, 6.74040856e-01, 8.44319398e-01],
           [2.73424568e-01, 6.78506237e-01, 8.43753286e-01],
           [2.81334256e-01, 6.82949866e-01, 8.43212501e-01],
           [2.89300487e-01, 6.87371790e-01, 8.42697759e-01],
           [2.97322950e-01, 6.91772047e-01, 8.42209159e-01],
           [3.05401043e-01, 6.96150593e-01, 8.41747760e-01],
           [3.13534922e-01, 7.00507378e-01, 8.41313818e-01],
           [3.21724493e-01, 7.04842291e-01, 8.40908330e-01],
           [3.29970207e-01, 7.09155200e-01, 8.40531785e-01],
           [3.38272224e-01, 7.13445925e-01, 8.40185338e-01],
           [3.46631304e-01, 7.17714259e-01, 8.39869540e-01],
           [3.55047646e-01, 7.21959964e-01, 8.39585861e-01],
           [3.63522125e-01, 7.26182769e-01, 8.39335051e-01],
           [3.72055103e-01, 7.30382386e-01, 8.39118625e-01],
           [3.80647037e-01, 7.34558508e-01, 8.38938059e-01],
           [3.89298695e-01, 7.38710800e-01, 8.38794540e-01],
           [3.98010198e-01, 7.42838936e-01, 8.38690044e-01],
           [4.06781767e-01, 7.46942588e-01, 8.38626428e-01],
           [4.15613501e-01, 7.51021428e-01, 8.38605675e-01],
           [4.24505482e-01, 7.55075132e-01, 8.38629760e-01],
           [4.33457177e-01, 7.59103429e-01, 8.38701226e-01],
           [4.42467980e-01, 7.63106074e-01, 8.38822592e-01],
           [4.51537005e-01, 7.67082867e-01, 8.38996531e-01],
           [4.60663043e-01, 7.71033673e-01, 8.39225882e-01],
           [4.69844540e-01, 7.74958428e-01, 8.39513630e-01],
           [4.79079573e-01, 7.78857156e-01, 8.39862897e-01],
           [4.88365838e-01, 7.82729982e-01, 8.40276911e-01],
           [4.97700643e-01, 7.86577140e-01, 8.40758984e-01],
           [5.07080909e-01, 7.90398989e-01, 8.41312477e-01],
           [5.16503178e-01, 7.94196019e-01, 8.41940760e-01],
           [5.25963637e-01, 7.97968860e-01, 8.42647174e-01],
           [5.35458139e-01, 8.01718284e-01, 8.43434985e-01],
           [5.44982251e-01, 8.05445212e-01, 8.44307339e-01],
           [5.54531293e-01, 8.09150707e-01, 8.45267214e-01],
           [5.64100395e-01, 8.12835974e-01, 8.46317378e-01],
           [5.73684558e-01, 8.16502350e-01, 8.47460344e-01],
           [5.83278719e-01, 8.20151295e-01, 8.48698337e-01],
           [5.92877814e-01, 8.23784377e-01, 8.50033255e-01],
           [6.02476849e-01, 8.27403257e-01, 8.51466653e-01],
           [6.12070961e-01, 8.31009672e-01, 8.52999717e-01],
           [6.21655379e-01, 8.34605437e-01, 8.54633318e-01],
           [6.31225620e-01, 8.38192398e-01, 8.56367920e-01],
           [6.40777591e-01, 8.41772397e-01, 8.58203557e-01],
           [6.50307461e-01, 8.45347293e-01, 8.60139944e-01],
           [6.59811748e-01, 8.48918928e-01, 8.62176457e-01],
           [6.69286927e-01, 8.52489212e-01, 8.64312378e-01],
           [6.78730317e-01, 8.56059905e-01, 8.66546441e-01],
           [6.88139761e-01, 8.59632678e-01, 8.68877062e-01],
           [6.97512366e-01, 8.63209411e-01, 8.71302979e-01],
           [7.06847103e-01, 8.66791547e-01, 8.73821989e-01],
           [7.16141794e-01, 8.70380828e-01, 8.76432447e-01],
           [7.25395984e-01, 8.73978567e-01, 8.79131915e-01],
           [7.34607710e-01, 8.77586468e-01, 8.81918675e-01],
           [7.43777175e-01, 8.81205667e-01, 8.84790069e-01],
           [7.52903803e-01, 8.84837491e-01, 8.87743855e-01],
           [7.61986655e-01, 8.88483364e-01, 8.90777991e-01],
           [7.71026197e-01, 8.92144306e-01, 8.93889905e-01],
           [7.80022463e-01, 8.95821439e-01, 8.97077287e-01],
           [7.88975595e-01, 8.99515838e-01, 9.00337853e-01],
           [7.97885859e-01, 9.03228521e-01, 9.03669347e-01],
           [8.06753631e-01, 9.06960454e-01, 9.07069544e-01],
           [8.15579373e-01, 9.10712555e-01, 9.10536265e-01],
           [8.24363623e-01, 9.14485700e-01, 9.14067378e-01],
           [8.33106968e-01, 9.18280725e-01, 9.17660808e-01],
           [8.41810037e-01, 9.22098432e-01, 9.21314538e-01],
           [8.50473477e-01, 9.25939595e-01, 9.25026615e-01],
           [8.59097578e-01, 9.29805083e-01, 9.28795277e-01],
           [8.67683055e-01, 9.33695606e-01, 9.32618673e-01],
           [8.76230770e-01, 9.37611811e-01, 9.36494970e-01],
           [8.84741157e-01, 9.41554460e-01, 9.40422531e-01],
           [8.93214216e-01, 9.45524445e-01, 9.44399908e-01],
           [9.01651102e-01, 9.49522259e-01, 9.48425322e-01],
           [9.10051557e-01, 9.53548851e-01, 9.52497488e-01],
           [9.18416194e-01, 9.57604867e-01, 9.56614869e-01],
           [9.26744955e-01, 9.61691167e-01, 9.60776163e-01],
           [9.35037937e-01, 9.65808553e-01, 9.64980024e-01],
           [9.43294771e-01, 9.69957981e-01, 9.69225246e-01],
           [9.51515411e-01, 9.74140292e-01, 9.73510497e-01],
           [9.59698535e-01, 9.78356779e-01, 9.77834789e-01],
           [9.67843737e-01, 9.82608418e-01, 9.82196767e-01],
           [9.75949164e-01, 9.86896714e-01, 9.86595395e-01],
           [9.84012514e-01, 9.91223356e-01, 9.91029585e-01],
           [9.92030980e-01, 9.95590254e-01, 9.95498132e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.freeze", N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
