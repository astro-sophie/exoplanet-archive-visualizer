import plotly.express as px


def create_mass_radius_plot(df, year):

    filtered_df = df[df['disc_year'] <= year ]
    plot_df = filtered_df.dropna(
        subset=['hostname', 'pl_name', 'pl_msinie', 'pl_rade', 'disc_year', 
         'disc_refname', 'discoverymethod', 'disc_facility', 
         'ra', 'dec', 'gaia_dr3_id']
    )
      
    fig = px.scatter(
        plot_df,
        x="pl_msinie",
        y="pl_rade",
        color="discoverymethod",
        title=f"Exoplanets Discovered up to {year}",
        labels={
            "pl_msinie": "Mass × sin(i)",
            "pl_rade": "Planet Radius",
            "discoverymethod": "Discovery Method"
        },
        hover_name="pl_name", 
        hover_data=['hostname','disc_year', 
         'disc_refname', 'disc_facility', 
         'ra', 'dec', 'gaia_dr3_id']
    )
    
    fig.update_xaxes(showspikes=True, spikecolor="green", spikesnap="cursor", spikemode="across")
    fig.update_yaxes(showspikes=True, spikecolor="orange", spikethickness=2)

    fig.update_layout(
        legend_title="Discovery Method"
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    
    fig.show()
    return fig