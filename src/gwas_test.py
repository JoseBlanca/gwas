import numpy
import pandas
import statsmodels.formula.api as smf
import statsmodels.api as sm


def create_gwas_test_pheno(mean, std_dev=1, size=100):
    return numpy.random.normal(mean, std_dev, size)


if __name__ == "__main__":
    print("Test")
    num_indis = 1000
    pheno_geno1 = create_gwas_test_pheno(1, size=num_indis)
    pheno_geno2 = create_gwas_test_pheno(1, size=num_indis)
    phenos = numpy.concatenate([pheno_geno1, pheno_geno2])
    genos = numpy.concatenate(
        [numpy.full((pheno_geno1.size,), 0), numpy.full((pheno_geno1.size,), 1)]
    )
    pheno_geno = pandas.DataFrame({"genotype": genos, "phenotype": phenos})
    model = smf.glm(
        "phenotype ~ C(genotype)",
        data=pheno_geno,
        family=sm.families.Gaussian(),
    ).fit()
    print(model.summary())
