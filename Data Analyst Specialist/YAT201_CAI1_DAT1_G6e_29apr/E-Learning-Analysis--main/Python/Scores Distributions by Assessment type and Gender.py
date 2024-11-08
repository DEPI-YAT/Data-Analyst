plt.figure(figsize=(14, 8))
sns.boxplot(x='assessment_type', y='score', hue='gender', data=merged_data, palette='Set2')
plt.title('Score Distribution by Assessment Type and Gender')
plt.xlabel('Assessment Type')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.show()
