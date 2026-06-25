import plotly.express as px


def create_mass_radius_plot(df, year):

    plot_df = df.dropna(
        subset=["pl_msinie", "pl_rade", "discoverymethod"]
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
        }
    )

    fig.update_layout(
        legend_title="Discovery Method"
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig
