from pycleanlens import cleanlens

model = cleanlens()
model.read_cleanset('source_poly1.par')
#model.imframe = '../../HST/snake_F160W.fits'
model.imframe = '../../Moments/snake_mom0.fits'
model.sframe = 'TEST_pycleanset.fits'
model.print_param()

model.draw_dwcs_region(output='south.dwcs',update=True)