from django.test import TestCase

content = '''
<p>Pellentesque elementum tellus id mauris faucibus, id sagittis mauris rhoncus. Donec ac iaculis dui, id convallis
    mauris. Fusce faucibus purus eu risus pulvinar, vel rutrum velit hendrerit. Sed urna nunc, efficitur faucibus
    sollicitudin non.</p>

<p>Nulla facilisi. Aenean pharetra fringilla nunc a finibus. Nulla vitae pretium nunc. Pellentesque sagittis
    sollicitudin turpis id aliquam. Cras lobortis diam in nunc posuere, et malesuada sem gravida. Curabitur ornare massa
    id orci faucibus elementum. Phasellus pharetra, velit <a href="#">in egestas rutrum,</a> metus dolor maximus massa,
    feugiat molestie eros mauris sit amet massa. Maecenas blandit diam lacus, in luctus nulla efficitur nec. Sed sit
    amet quam sit amet odio scelerisque vestibulum vel sit amet ante. Cras fringilla efficitur lacinia. Cras posuere,
    arcu id consequat ultrices, urna urna cursus massa, at sollicitudin elit lacus quis dui. In laoreet nulla a turpis
    blandit sollicitudin. Donec in risus eu lorem volutpat hendrerit quis non lorem. Nulla in metus ipsum.
<p>Etiam sit amet augue non velit aliquet consectetur. Proin gravida, odio in facilisis pharetra, neque enim aliquam
    eros, vitae gravida orci elit vel magna. Integer viverra a purus id gravida. Donec laoreet mi ac auctor ultricies.
    Pellentesque ullamcorper est et erat ullamcorper gravida. In hac habitasse platea dictumst. Pellentesque justo
    mauris, mollis at tortor ut, commodo venenatis elit. Curabitur suscipit pellentesque nunc, id tempus mi facilisis
    sed. Curabitur molestie eu odio vitae condimentum. Donec placerat tristique neque a blandit. Nullam commodo massa ut
    eros elementum, in suscipit libero aliquam.</p>

<h4>Sed id sodales sapien. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla facilisi.</h4>
<p>Nulla facilisi. Duis auctor fringilla sagittis. Fusce ornare, dui id consequat volutpat, nibh metus viverra nibh,
    vitae bibendum diam velit in libero. Sed dignissim quam sit amet nibh porttitor, non pellentesque metus tincidunt.
    Maecenas non velit sapien. </p>
<p>Maecenas vel dolor sit amet ligula interdum tempor id eu ipsum. Suspendisse pharetra risus ut metus elementum
    pulvinar. Mauris eget varius tellus. Cras et lorem vel nunc gravida porttitor.</p>
<blockquote>
    Free Responsive HTML5 &amp; CSS3 Magazine Template
</blockquote>
<p>Ut est elit, vehicula tempus volutpat ut, sodales eget odio. Nunc placerat, orci ac iaculis feugiat, sem tellus
    efficitur tortor, mollis iaculis lacus ante nec risus. Sed consequat vehicula pretium.</p>
'''

# for i in range(1, 31):
#     Blog.objects.create(
#         category_id=1,
#         title=f'{i}: Lorem Ipsum Dolor Sit Consectetur Adipisicing',
#         description=f'{i}: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitat...',
#         content=content
#         )

