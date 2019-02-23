
def clean_complex(z):
    s = str(z).replace('j','i')
    if (s[0] == '('): 
        s = s[1:-1]
    if (z.real == 0):
        s = '0+' + s
    return s

def export_sim(sim, file_name, do_df, do_hull):
    with open(file_name, 'w') as file:
        fields = ['t']
        if do_df:
            fields.append('lambda(t)')
        if do_hull:
            fields.append('hull')  
        file.write(','.join(fields) + '\n')
        
        for i in range(sim.sample_count):
            values = [str(sim.time_domain[i])]
            if do_df:
                values.append(str(sim.samples[i]))
            if do_hull:
                values.append(clean_complex(sim.hull[i]))
            file.write(','.join(values) + '\n')
