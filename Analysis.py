big_array = np.asarray(biglist)

values = (big_array > test).sum()

print("The probability of your roll being higher than", test, "is", values * 100 / iterations, "%")
print("The standard deviation is", np.std(big_array))
print("The mean is", np.mean(big_array))

plt.hist(big_array,
         bins=np.arange(min(big_array) - 0.5,
                        max(big_array) + 1.5, 1.0),
         edgecolor="k")
plt.show()
